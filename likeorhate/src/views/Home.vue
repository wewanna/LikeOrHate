<style>
  .good {
    background-color: #c7ffd4;
    color: black;
  }

  .bad {
    background-color: #ffc9d5;
    color: black;
  }
  .default {
    color: black;
  }
</style>
<template>
  <v-container name="home-container">
    <v-toolbar app>
      <v-toolbar-title class="headline text-uppercase">
        <span>like-or-hate</span>
        <span class="text-lowercase font-weight-light"> : text emotion classifier</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn flat color="teal" value="classify" @click="processText">
        <v-icon>done</v-icon>
        <span> Classify</span>
      </v-btn>
      <input type="file" ref="file" style="display: none" @change="onFileChange" accept="text/plain">
      <v-btn flat color="teal" value="openfile" @click="$refs.file.click()">
        <v-icon>open_in_new</v-icon>
        <span> Open File</span>
      </v-btn>
    </v-toolbar>

    <v-layout>
      <v-card height="430" width="100%" style="overflow:scroll;">
        <div id="view" style="margin: 10px">
        </div>
      </v-card>
    </v-layout>

    <v-layout wrap>
      <v-flex xs>
        <v-textarea
          v-model="text"
          name="editor"
          label="Type text to classify"
          no-resize=""
          rows="7"
        ></v-textarea>
      </v-flex>
    </v-layout>
  </v-container>

</template>

<script>
  import axios from 'axios'
  import fs from 'fs'

  export default {
    components: {},
    data: () => {
      return {
        highligted: '',
        text: ''
      }
    },
    methods: {
      onFileChange (e) {
        let files = e.target.files || e.dataTransfer.files
        if (files.length === 0) {
          return
        }
        fs.readFile(files[0].path, 'utf8', (err, data) => {
          if (err) {
            console.log(err)
            this.text = 'cannot read file'
          } else {
            this.text = data
          }
          e.value = ''
        })
        console.log(files[0])
      },
      processText () {
        let splited = this.text.split('.')
        this.highligted = this.text
        async function getData (param) {
          try {
            let res = await axios({
              method: 'post',
              url: 'http://127.0.0.1:5000',
              timeout: 8000,
              data: { text: param }
            })
            if (res.status !== 200) {
              // test for status you want, etc
              console.log(res.status)
              this.highligted = 'invalid text'
              return
            }
            // Don't forget to return something
            let result = 0
            console.log(res.data)
            if (res.data === '긍정적') {
              result = 1
            } else if (res.data === '오류') {
              result = 2
            }
            return { data: result, text: param }
          } catch (err) {
            console.error(err)
            this.highligted = 'error'
          }
        }

        async function makeSpanned () {
          let types = ['bad', 'good', 'default']
          let spanned = ''
          for (let i in splited) {
            await getData(splited[i]).then((res) => {
              console.log(res)
              spanned += '<span class="' + types[res.data] + '">' + res.text + '</span>'
            })
          }
          console.log('result: ' + spanned)
          return spanned
        }

        makeSpanned().then(text => {
          document.getElementById('view').innerHTML = text
          console.log(text)
        })
      }
    }
  }
</script>

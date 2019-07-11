<style>
  good {
    background-color: blue;
    color: white;
  }
  bad {
    background-color: red;
    color: white;
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
      <v-btn flat color="teal" value="openfile">
        <v-icon>open_in_new</v-icon>
        <span> Open File</span>
      </v-btn>
    </v-toolbar>

    <v-layout>
      <v-card height="430" width="100%" style="overflow:scroll;">
        <div style="margin: 10px">
          {{highligted}}
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
  export default {
    components: {},
    data: () => {
      return {
        highligted: '',
        text: ''
      }
    },
    methods: {
      processText () {
        let splited = this.text.split('.')
        let result = ''
        let type = ''
        splited.forEach(function (element) {
          console.log(element)
          axios.post('http://localhost:5000', { text: element }).then(res => {
            if(res.status !== 200) {
              this.highligted = 'invalid text'
              return
            }


            if(res.data === '긍정적')
              type = 'good'
            else
              type = 'bad'
            result += '<span class=' + type + '>' + element + '</span>'
          })
        })
        this.highligted = result
      }
    }
  }
</script>

<template>
  <v-app>
    <v-content>
      <router-view/>
    </v-content>
    <v-card flat>
      <v-bottom-nav :value="true" fixed absolute color="transparent">
        <v-btn color="teal" flat value="recent" to="/">
          <span>Home</span>
          <v-icon>home</v-icon>
        </v-btn>
        <v-btn color="teal" flat value="favorites" to="/about">
          <span>About</span>
          <v-icon>info</v-icon>
        </v-btn>
      </v-bottom-nav>
    </v-card>
  </v-app>
</template>

<script>

  export default {
    name: 'App',
    components: {},
    data: () => {
      return {
        //
      }
    }
  }
</script>

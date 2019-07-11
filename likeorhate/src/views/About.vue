<style>
  .cards {
    width: 50%;
    margin: 10px;
    height: 70vh;
  }
  .in-cards {
    margin: 15px;
  }
</style>
<template>
  <v-layout>
    <v-toolbar app>
      <v-toolbar-title class="headline text-uppercase">
        <span>like-or-hate</span>
        <span class="text-lowercase font-weight-light"> : text emotion classifier</span>
      </v-toolbar-title>
    </v-toolbar>
    <v-container fill-height>
      <v-card class="cards">
        <div class="in-cards">
          <span class="headline">함종현</span>
        </div>
      </v-card>
      <v-card class="cards">
        <div class="in-cards">
          <span class="headline">LikeOrHate</span>
        </div>
      </v-card>
      <v-card class="cards">
        <div class="in-cards">
          <span class="headline">박철완</span>
        </div>
      </v-card>
    </v-container>
  </v-layout>
</template>

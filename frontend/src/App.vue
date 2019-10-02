<template>
  <v-app v-if="currentView !== undefined" :currentView="currentView" id="inspire">
    <link href="https://use.fontawesome.com/releases/v5.0.13/css/all.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css?family=Material+Icons" rel="stylesheet">
    <v-navigation-drawer
      v-model="drawer"
      app
      clipped
    >
      <v-list  dense>
        <v-list-item @click="">
          <v-list-item-action>
            <v-icon>fa-check</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Review</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item @click="">
          <v-list-item-action>
            <v-icon>note_add</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Add notes</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-group
          prepend-icon="layers"
          value="false"
        >
          <template v-slot:activator>
            <v-list-item-title>Decks</v-list-item-title>
          </template>
          <v-list-item @click="">
            <v-list-item-action>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>Vue.js</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
          <v-list-item @click="">
            <v-list-item-action>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>PyTorch</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
          <v-list-item @click="">
            <v-list-item-action>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>Rust</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list-group>
      </v-list>
    </v-navigation-drawer>
    <v-app-bar
      app
      clipped-left
    >
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title>CodeMems</v-toolbar-title>
    </v-app-bar>

    <v-content :currentView="currentView">
      <Welcome v-show="currentView === 'welcome'"></Welcome>
      <Stats v-show="currentView === 'stats'"></Stats>
    </v-content>

    <v-footer app>
      <span>&copy; 2019</span>
    </v-footer>
  </v-app>
</template>

<script>
  import Welcome from "./components/Welcome"
  import Stats from "./components/Stats"
  import { mapGetters } from "vuex"
  export default {
    components: {
      Welcome,
      Stats,
    },
    data: () => ({
      drawer: null,
    }),
    computed: {
      ...mapGetters([
        "currentView"
      ])
    },
    created () {
      this.$vuetify.theme.dark = true
    },
  }
</script>

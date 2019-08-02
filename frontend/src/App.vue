<template>
  <v-app v-if="currentView !== undefined" :currentView="currentView" id="inspire">
    <link href="https://use.fontawesome.com/releases/v5.0.13/css/all.css" rel="stylesheet">
    <v-navigation-drawer
      v-model="drawer"
      app
      clipped
    >
      <v-list dense>
        <v-list-item @click="">
          <v-list-item-action>
            <v-icon>dashboard</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Dashboard</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item @click="">
          <v-list-item-action>
            <v-icon>settings</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Settings</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-app-bar
      app
      clipped-left
    >
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title>Application</v-toolbar-title>
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

<template>
  <v-app v-if="currentView !== undefined" :currentView="currentView" id="inspire">
    <link href="https://use.fontawesome.com/releases/v5.0.13/css/all.css" rel="stylesheet">
    <AppDrawer/>
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
  import AppDrawer from "./components/AppDrawer"
  import { mapGetters } from "vuex"
  export default {
    components: {
      Welcome,
      Stats,
      AppDrawer,
    },
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

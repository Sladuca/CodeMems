<template lang="html">
  <v-container
    fluid
    fill-height
  >
    <v-layout
      align-center
      justify-center
    >
      <v-flex shrink>
        <v-tooltip right>
          <template v-slot:activator="{ on }">
            <v-btn
              icon
              large
              target="_blank"
              @click="gotoStats()"
            >
              <v-icon large>fa-chart-line</v-icon>
            </v-btn>
          </template>
          <span>Stats</span>
        </v-tooltip>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
export default {
  name: "Welcome",
  methods: {
    ...mapActions([
      "changeView"
    ]),
    ...mapGetters([
      "currentView"
    ]),
    gotoStats () {
      this.changeView("stats")
    }
  }
}
</script>

<style lang="css" scoped>
</style>

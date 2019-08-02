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
              v-on="gotoWelcome()"
            >
              <v-icon large>fa-sticky-note</v-icon>
            </v-btn>
          </template>
          <span>Notes</span>
        </v-tooltip>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
export default {
  name: "Stats",
  methods: {
    ...mapActions([
      "changeView"
    ]),
    ...mapGetters([
      "currentView"
    ]),
    gotoWelcome () {
      this.changeView("welcome")
    }
  }
}
</script>

<style lang="css" scoped>
</style>

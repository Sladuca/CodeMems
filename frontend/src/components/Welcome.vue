<template lang="html">
  <v-container
    fill-height
  >
    <v-layout
      align-top
      justify-center
    >
      <v-flex>
        <template>
          <!-- Welcome message card --> 
          <v-card
           class="pa-4 md-4"
          >
            <v-card-title>
              Welcome back, Sebastien. Are your hacker senses tingling?
            </v-card-title>
            <v-card-text>
              You have 3 decks with cards to review, for a total of 99 cards
            </v-card-text>
            <v-card-actions>
              <v-btn text>
                Review Now
              </v-btn>
            </v-card-actions>
          </v-card>
          <!-- end message card -->
          <v-divider></v-divider>
          <Decks></Decks>
        </template>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import Decks from './Decks.vue'
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
  },
  components: {
    Decks
  }
}
</script>

<style lang="css" scoped>
</style>

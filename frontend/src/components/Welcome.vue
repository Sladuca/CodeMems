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
          <!-- Deck items --> 
          <v-expansion-panels
            class="pa-4 md-4"
            >
            <v-expansion-panel
              v-for="(item, i) in 3"
              :key="i"
            >
            <v-expansion-panel-header>
              <v-badge
                :left=true
                >
                <template v-slot:badge>33</template>
                <span>Deck_Name</span>
              </v-badge>
            </v-expansion-panel-header>
            <v-expansion-panel-content>
              Review
            </v-expansion-panel-content>
            </v-expansion-panel>
          </v-expansion-panels>
        </template>
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

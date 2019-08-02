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
              v-on="on"
            >
              <v-icon large>mdi-code-tags</v-icon>
            </v-btn>
          </template>
          <span>Source</span>
        </v-tooltip>
        <v-tooltip right>
          <template v-slot:activator="{ on }">
            <v-btn
              icon
              large
              href="https://codepen.io/johnjleider/pen/bXNzZL"
              target="_blank"
              v-on="on"
            >
              <v-icon large>mdi-codepen</v-icon>
            </v-btn>
          </template>
          <span>Codepen</span>
        </v-tooltip>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
export default {

}
</script>

<style lang="css" scoped>
</style>

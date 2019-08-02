<template lang="html">
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
</template>

<script>
export default {
  name: "AppDrawer",
  data: () => ({
    drawer: null,
  }),
}
</script>

<style lang="css" scoped>
</style>

import Vuex from 'vuex';
import Vue from 'vue';
import notes from './modules/notes';

// load Vuex
Vue.use(Vuex);

// create store
export default new Vuex.Store({
  modules: {
    notes,
  } 
});

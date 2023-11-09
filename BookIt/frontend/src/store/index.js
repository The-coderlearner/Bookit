import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    user_id: localStorage.getItem('user_id') || null,
    access_token: localStorage.getItem('access_token') || null,
    userType:  localStorage.getItem('user_type') || null,
  },
  getters: {
    USER_ID(state) {
      return state.user_id
    },
    TOKEN(state) {
      return state.access_token
    },
    USER_TYPE(state) {
      return state.userType
    }
  },
})


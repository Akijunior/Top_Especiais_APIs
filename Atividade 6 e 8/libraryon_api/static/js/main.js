// main.js
import axios from 'axios'
import VueAxios from 'vue-axios'
import jwt_decode from 'jwt-decode'
import Vuex from 'vuex'
Vue.use(Vuex);
Vue.use(VueAxios, axios);
// WE WILL ADD THE CODE LATER
// YOUR VUE INSTANCE

const store = new Vuex.Store({
  state: {
    jwt: localStorage.getItem('t'),
    endpoints: {
      obtainJWT: 'http://localhost/auth/obtain_token',
      refreshJWT: 'http://localhost/auth/refresh_token'
    }
  },
  mutations: {
    updateToken(state, newToken){
      localStorage.setItem('t', newToken);
      state.jwt = newToken;
    },
    removeToken(state){
      localStorage.removeItem('t');
      state.jwt = null;
    }
  },
  actions:{
    obtainToken(username, password){
      const payload = {
        username: username,
        password: password
      }
      axios.post(this.state.endpoints.obtainJWT, payload)
        .then((response)=>{
            this.commit('updateToken', response.data.token);
            alert("Foi");
          })
        .catch((error)=>{
            console.log(error);
            alert("Não foi");
          })
    },
    refreshToken(){
      const payload = {
        token: this.state.jwt
      }
      axios.post(this.state.endpoints.refreshJWT, payload)
        .then((response)=>{
            this.commit('updateToken', response.data.token)
          })
        .catch((error)=>{
            console.log(error)
          })
    },
    inspectToken(){
      const token = this.state.jwt;
      if(token){
        const decoded = jwt_decode(token);
        const exp = decoded.exp
        const orig_iat = decode.orig_iat
        if(exp - (Date.now()/1000) < 1800 && (Date.now()/1000) - orig_iat < 628200){
          this.dispatch('refreshToken')
        } else if (exp -(Date.now()/1000) < 1800){
          // DO NOTHING, DO NOT REFRESH
        } else {
          // PROMPT USER TO RE-LOGIN, THIS ELSE CLAUSE COVERS THE CONDITION WHERE A TOKEN IS EXPIRED AS WELL
        }
      }
    }
  }
  })
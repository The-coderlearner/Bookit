<template>
    <div class="navBar">
      <nav class="navbar navbar-expand-lg navbar-light bg-light" style="background: linear-gradient(to right, #ee7724, #d8363a, #dd3675, #b44593);">
    &emsp;
    <router-link :to="'/' + data.username +'/profile/view/summary' " class="navbar-brand">
      <img src="https://static.vecteezy.com/system/resources/previews/005/544/718/original/profile-icon-design-free-vector.jpg" alt="Oops! no image is found" class="nav_avatar">
    </router-link>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav mr-auto">
        <li class="nav-item active">
          <router-link :to="'/admin/' + data.username" class="nav-link">Home <span class="sr-only">(current)</span></router-link>
        </li>
        <li>
          <form @submit.prevent="logOut">
            <button class="btn btn-outline-success my-2 my-sm-0" id="color" type="submit">Logout</button>
          </form>
        </li>
      </ul>
    </div>
  </nav>
    </div>
  </template>
  
  <script>
  import { ref } from 'vue';
  import { useRouter } from 'vue-router';
  export default {
    setup(){
      const router = useRouter();

      const data = ref({
        username:  router.currentRoute.value.params.username

      });

      const logOut = async() => {
        data.username =  router.currentRoute.value.params.username
        localStorage.setItem('access_token', '');
        localStorage.setItem('id', '');
        localStorage.setItem('name', '');
        localStorage.setItem('user_type','');
        router.push({name: 'adminLogin'})
      }
      return {
        data,
        logOut
      }
    },
  };
  </script>
  
<style scoped>
  .nav_avatar{
        width: 30px;
        object-fit: contain;
        align-self: flex-start;
  }
  #mycolor{
        background-color:white;
        border-color: orange;
        color: orange;
  }
  #color{
        align-content: initial;
        background-color: lightsalmon;
    }
  
</style>
  
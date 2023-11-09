<template>
    <nav class="navbar navbar-expand-lg navbar-light bg-light" style="background: linear-gradient(to right, #ee7724, #d8363a, #dd3675, #b44593);">
      <div class="container" >
        <!-- Brand Logo -->
        <router-link :to="'/' + data.username" class="navbar-brand">
          <img src="https://static.vecteezy.com/system/resources/previews/005/544/718/original/profile-icon-design-free-vector.jpg" alt="User Profile" class="nav_avatar">
        </router-link>
  
        <!-- Toggler Button for Small Screens -->
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
  
        <!-- Navbar Links -->
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <router-link :to="'/' + data.username + '/home'" class="nav-link">Home</router-link>
            </li>
            <li class="nav-item">
              
            </li>
          </ul>
  
          <!-- Search Form -->
          <form class="d-flex" @submit.prevent="search">
            <input class="form-control me-2" v-model="searchValue" type="search" placeholder="Search" aria-label="Search">
            <button class="btn btn-outline-success" id="mycolor" type="submit" style="margin-right:5px" >Search</button>
          </form>
  
          <!-- Logout Button -->
          <form @submit.prevent="logOut">
            <button class="btn btn-outline-success" id="color" type="submit">Logout</button>
          </form>
        </div>
      </div>
    </nav>
  </template>
  
  <script>
  import axios from 'axios';
  import { ref } from 'vue';
  import { useRouter } from 'vue-router';
  
  export default {

    setup() {
      const router = useRouter();
      const searchValue = ref('');
      const data = ref({
        username:  router.currentRoute.value.params.username

      })
  
      const logOut = async () => {
        localStorage.setItem('access_token', '');
        localStorage.setItem('id', '');
        localStorage.setItem('user_type', '');
        router.push({name: 'logIn'})
      }
      
      const search = async () => {
        try {
          
          const response = await axios.post('http://127.0.0.1:5000/searchit', searchValue.value, {
            headers: { 'Content-Type': 'application/json' },
          });
          console.log('Searching for:', searchValue.value);
          console.log('Search response:', response.data); // Use response.data to access the response data
          
          // Assuming you want to pass data.username as a parameter to the searchResult route
          router.push({ name: 'searchResult', params: { username: data.username, sv: searchValue.value } });
        } catch (error) {
          console.error('Error searching:', error);
        }
      };

      return {
        searchValue,
        data,
        logOut,
        search
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
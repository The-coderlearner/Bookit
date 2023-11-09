<template>

    <div class="searchResult">
        <navbarUser></navbarUser>
      <h1 class="text-center mb-4">{{ sv }}</h1>
      <!-- Shows Section -->
      <div class="row justify-content-center">
        <div class="col-md-12">
          <h3 class="text-center mb-4">Shows</h3>
          <hr />
          <div class="row">
            <div class="col-md-4 mb-4" v-for="show in L" :key="show.ID">
              <div class="card">
                <img :src="show.imgURL" class="card-img-top" alt="Show Image" />
                <div class="card-body">
                  <h5 class="card-title">{{ show.Name }}</h5>
                  <p></p>
                  <router-link :to="'/' + username + '/home/' + show.ID" class="btn btn-primary">
                    Book Now
                  </router-link>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
  
      <!-- Venue Section -->
      <div class="row justify-content-center">
        <div class="col-md-12">
          <h3 class="text-center mb-4">Venue</h3>
          <hr />
          <div class="row">
            <div class="col-md-4 mb-4" v-for="venue in v" :key="venue.ID">
              <div class="card">
                <img :src="venue.imgURL" class="card-img-top" alt="Venue Image" />
                <div class="card-body">
                  <h5 class="card-title">{{ venue.Name }}</h5>
                  <button @click.prevent="viewmore(venue.ID)" class="btn btn-primary">
                    View more
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>

  import axios from 'axios';

  export default {
    name: 'searchResult',
    data() {
      return {
        sv: '',
        L: [],
        v: [],
        username: this.$route.params.username,
      };
    },
    methods: {
        viewmore(venueid){
            console.log(venueid)
            this.$router.push(`/${this.username}/venue/${venueid}`);
        },
    },

    mounted(){
        axios.get('http://127.0.0.1:5000/searchit')
        .then(response => {
          
          var m = response.data;
          this.sv = m[0];
          this.L = m[2];
          this.v = m[1];
          console.log(this.sv);
        })
        .catch(error => {
          console.error('Error fetching venues:', error);
        });
    },
  };
  </script>
  
  <style>

  </style>
  
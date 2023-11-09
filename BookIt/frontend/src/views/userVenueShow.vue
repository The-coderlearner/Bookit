<template>
    <div>
        <navbarUser></navbarUser>
      <h1 class="text-center mb-4">{{ Venue }}</h1>
      <h5 class="text-center mb-4">{{ place }}</h5>
      <div class="row justify-content-center">
        <div class="col-md-4 mb-4" v-for="show in L" :key="show.ID">
          <div class="card">
            <div class="card">
              <img :src="show.imgURL" class="card-img-top" alt="Show Image" />
              <div class="img__overlay">
                <p class="img__description">{{ show.Description }}</p>
              </div>
            </div>
            <div class="card-body">
              <h5 class="card-title">{{ show.Name }}</h5>
              <router-link :to="'/' + username + '/home/' + show.ID" class="btn btn-primary">
                Book
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
import axios from 'axios'

  export default {
    data() {
        return{
            Venue: '',
            place: '',
            L: [],
            username: this.$route.params.username,
            venue_id: 0,
        }
      
    },

    mounted(){
        const venueid = this.$route.params.venueid;
        console.log(venueid)
        axios.get(`http://127.0.0.1:5000/uservenue/${venueid}`)
        .then(response => {
          var m = response.data;
          this.venue_id = m[0];
          this.Venue = m[1];
          this.place = m[2];
          this.L = m[3]
          console.log(venueid)

        })
        .catch(error => {
          console.error('Error fetching venues:', error);
        });
    },
  };
  </script>
  
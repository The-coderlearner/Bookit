<template>
    <div class="userProfile">
    <div class="container-fluid">
      <navbarUser></navbarUser>
      <div class="row">
        <div class="col-15 text-center">
          <h1>{{ username }}</h1>
        </div>
      </div>
      <p></p>
      <div class="row">
        <template v-if="showsdone.length === 0 && shows.length === 0">
          <h5 class="card-title">Nothing Here... To book shows click Home :D</h5>
        </template>
        <template v-else>
          <div v-for="i in shows" :key="i.ID" class="col-4">
            <div class="card-deck">
              <div class="card">
                <img
                  class="card-img-top"
                  :src="i.imgURL"
                  :alt="'Movie ' "
                  />
                <div class="card-body">
                  <h5 class="card-title">{{ i.Name }}</h5>
                  <h6 class="card-title">Venue: {{ i.Venue }}</h6>
                  <p class="card-text">Date: {{ i.Date }}</p>
                  <p class="card-text">No. of seats: {{ i.nos }}</p>
                  <p class="card-text">Total Price: ₹{{ i.Total }}</p>
                </div>
              </div>
            </div>
          </div>
          <div v-for="i in showsdone" :key="i.ID" class="col-4">
            <div class="card-deck">
              <div class="card">
                <img
                  class="card-img-top"
                  :src="i.imgURL"
                  :alt="'Movie ' "
                  style="-webkit-filter: grayscale(100%); filter: grayscale(100%);"
                  />
                  <div class="card-body">
                  <h5 class="card-title">{{ i.Name }}</h5>
                  <h6 class="card-title">Venue: {{ i.Venue }}</h6>
                  <p class="card-text">Date: {{ i.Date }}</p>
                  <p class="card-text">No. of seats: {{ i.nos }}</p>
                  <p class="card-text">Total Price: ₹{{ i.Total }}</p>
                  <button class="btn btn-primary" @click="initRate(i)"  data-bs-toggle="modal" data-bs-target="#rateModal">Rate</button>
                </div>
              </div>
            </div>
          </div>
        </template>
      </div>
      
    </div>
    <div class="modal fade" id="rateModal" tabindex="-1" aria-labelledby="rateModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="rateModalLabel">Book</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <form  @submit.prevent="rateIt">
                <div class="mb-3">
                <label for="form-Ratings-input" class="form-label">Ratings:</label>
                <input
                  id="form-Ratings-input"
                  type="text"
                  v-model="rate"
                  class="form-control"
                  required
                  placeholder="Enter Ratings"
                />
                </div>
              <!-- Modal footer with Close button -->
              <div class="modal-footer">
                <button type="submit" class="btn btn-secondary" data-bs-dismiss="modal">Submit Rating</button>
              </div>
            </form>
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
            username: '',
            shows: [],
            showsdone: [],
            rate: 0,
            id:0,
        }
      
    },

    mounted() {
        const username = this.$route.params.username
      this.username = username
      console.log(username)
      axios.get(`http://127.0.0.1:5000/${this.username}/profile`)
        .then(response => {
          this.showsdone = response.data.shows;
          this.shows = response.data.showsdone;
          console.log(response.data.shows)
        })
        .catch(error => {
          console.error('Error fetching venues:', error);
        });
    },
    methods:{
        initRate(i){
            this.id = i.ID;
            this.rate = i.Rating
        },
        rateIt(){
            const payload = {
                Rating: this.rate,
                Username: this.username,
                ID: this.id
            }
            axios.put(`http://127.0.0.1:5000/${this.username}/profile`, payload)
            .then(() => {
            window.location.reload()
            })
            .catch(error => {
            console.error('Error fetching values:', error);
            });
            }
    }

  };
  </script>
  
  
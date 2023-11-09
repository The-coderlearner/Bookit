<template>
  <div class="bookShow">
    <navbarUser></navbarUser>
    <div class="jumbotron jumbotron-fluid bg-dark text-white">
      <div class="container">
        <h1 class="display-3">{{ show }}</h1>
        <h3 class="display">{{ vename }}</h3>
      </div>
    </div>
    <form>
      <div class="container mt-5">
        <b-alert variant="success" v-if="showMessage" show>{{ message }}</b-alert>

        <div class="row">
          <div class="col-md-4">
            <div class="card">
              <div class="card-header">
                <h4 class="mb-0">About movie</h4>
              </div>
              <div class="card-body">
                <p variant="success" v-if="nomoreseats" show><b>Housefull</b></p>
                <p class="lead"><b>Tags </b></p>
                <p><i>{{ tag }}</i></p>
                <p class="lead"><b>Ratings</b></p>
                <p><i>{{ r }}/10</i></p>
              </div>
            </div>
          </div>
          <div class="col-md-4">
            <div class="card">
              <div class="card-header">
                <h4 class="mb-0">Dates</h4>
              </div>
              <div class="card-body">
                <select name="date" class="form-control">
                  <option v-for="i in date" :key="i">{{ i }}</option>
                </select>
              </div>
            </div>
          </div>
          <div class="col-md-4">
            <div class="card">
            <div class="card-header">
                <h4 class="mb-0">Book Now</h4>
              </div>
              <div class="card-body">
                <button @click.prevent="initBook()" data-bs-toggle="modal" data-bs-target="#bookShowModal" class="btn btn-primary" name="showprice">Book</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </form>
    <div class="modal fade" id="bookShowModal" tabindex="-1" aria-labelledby="bookShowModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="bookShowModalLabel">Book</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <form  @submit.prevent="bookTicket">
              <div class="mb-3">
                <label for="form-seat-input" class="form-label">Select Number of Seats:</label>
                <select name="nob" class="form-control" v-model="selectedSeats">
                  <option v-if="Z > 5" :selected="true">{{ sn }}</option>
                  <option v-for="i in (Z > 10 ? 10 : Z)" :key="i">{{ i }}</option>
                </select>
              </div>
              <div class="mb-3">
                <label class="form-label">Price:</label>
                <p>{{ p }}</p>
              </div>
              <div class="mb-3">
                <label class="form-label">Grand Total:</label>
                <p>{{ totalPrice }}</p>
              </div>
              <!-- Modal footer with Close button -->
              <div class="modal-footer">
                <button type="submit" class="btn btn-secondary" data-bs-dismiss="modal">Pay</button>
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
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
import { useRouter } from 'vue-router';
  export default {
    
    data() {
      return {
        router: useRouter(),
        showid:0,
        nomoreseats: false,
        showMessage :false,
        message: "Successfully booked",
        show: '', 
        vename: '', 
        Z: 0, 
        tag: '',
        r: 0, 
        date: [], 
        sn: 0, // Set sn data here
        p: 0,
        username: '', 
        selectedSeats: 0,
      };
    },
    computed: {
    totalPrice() {
      return this.selectedSeats * this.p;
    },
  },
    mounted() {
    const shid = this.$route.params.showid
      this.showid = shid
      this.username = this.$route.params.username
      this.axios.get(`http://127.0.0.1:5000/${this.showid}`)
      .then(response=>{
        var k = response.data;
        console.log(k)
        this.show = response.data[3]
        this.vename = response.data[1];
        this.tag = response.data[6];
        this.r = response.data[2];
        this.date = response.data[7];
        this.Z = response.data[4];
        console.log(this.Z)
        this.p = response.data[5];
        if (this.Z<=0){
            this.nomoreseats = true;
        }
      }).catch(error => {
          console.error('Error fetching details:', error);
        });
    },

    methods: {
        initBook(){
            this.selectedSeats = 0;
       
      },

      bookTicket() {
        if (confirm('Are you sure you want to Book it?')){
            axios.post(`http://127.0.0.1:5000/${this.showid}/${this.selectedSeats}/${this.username}/${this.totalPrice}`)
            .then(() => {
                this.showMessage = true;
                this.router.push({ name: 'userHome' });
            })
            .catch((error) => {
              console.log(error);
            });
        
        
        }
        
      },
    },
    
  };
  </script>
  
  <style scoped>
  /* Your component-specific styles here */
  </style>
  
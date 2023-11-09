<template>
    <div class="adminHome">
      <navBar></navBar>
  
      <section class="container my-5">
      <h1 class="text-center mb-4">Available Venues</h1>
      <div class="row justify-content-center">
        <b-alert variant="success" v-if="showMessage" show>{{ message }}</b-alert>

        <!-- Venue Cards -->
        <div v-for="venue in venues" :key="venue.ID" class="col-md-4 mb-4">
          <div class="card">
            <img :src="venue.imgURL || 'https://via.placeholder.com/350x200'" class="card-img-top" alt="Show Image">
            <div class="card-body">
              <h5 class="card-title">{{ venue.name }}</h5>
              <p class="card-text">{{ venue.place }}</p>

              <div class="d-flex justify-content-between">
                <button @click.prevent="venInit(venue)" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#editVenueModal">Edit Venue</button>
                <button @click.prevent="deleteVenue(venue)" class="btn btn-primary">Delete</button>
                <router-link :to="`/admin/${username}/${venue.ID}`"><button class="btn btn-primary">View Shows</button> </router-link>
              </div>
            </div>
          </div>
        </div>
        <!-- End Venue Cards -->

        <!-- Add Venue Button -->
        <div class="col-md-4 mb-4">
          <div class="card">
            <img src="https://via.placeholder.com/350x200" class="card-img-top" alt="Show Image">
            <div class="card-body text-center">
              <button class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#addVenueModal">
                  Add Venue
                </button>
            </div>
          </div>
        </div>
        <!-- End Add Venue Button -->
      </div>
    </section>
    <!-- End Available Venues Section -->
      <!-- Modal -->
      <div class="modal fade" id="addVenueModal" tabindex="-1" aria-labelledby="addVenueModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="addVenueModalLabel">Add a new Venue</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <form @submit.prevent="addVen">
              <div class="mb-3">
                <label for="form-title-input" class="form-label">Title:</label>
                <input
                  id="form-title-input"
                  type="text"
                  v-model="addVenue.Name"
                  class="form-control"
                  required
                  placeholder="Enter Name"
                />
              </div>
              <div class="mb-3">
                <label for="form-capacity-input" class="form-label">Capacity:</label>
                <input
                  id="form-capacity-input"
                  type="text"
                  v-model="addVenue.Capacity"
                  class="form-control"
                  required
                  placeholder="Enter Capacity"
                />
              </div>
              <div class="mb-3">
                <label for="form-place-input" class="form-label">Place:</label>
                <input
                  id="form-place-input"
                  type="text"
                  v-model="addVenue.Place"
                  class="form-control"
                  required
                  placeholder="Enter Place"
                />
              </div>
              <div class="mb-3">
                <label for="form-imgURL-input" class="form-label">imgURL:</label>
                <input
                  id="form-imgURL-input"
                  type="text"
                  v-model="addVenue.imgURL"
                  class="form-control"
                  required
                  placeholder="Enter imgURL"
                />
              </div>
              <!-- Modal footer with Save and Close buttons -->
              <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                <button type="submit" class="btn btn-primary">Save Venue</button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>


     <!-- Modal Edit -->
     <div class="modal fade" id="editVenueModal" tabindex="-1" aria-labelledby="editVenueModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="editVenueModalLabel">Edit Venue</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <form @submit.prevent="editVen">
              <div class="mb-3">
                <label for="form-title-input" class="form-label">Title:</label>
                <input
                  id="form-title-input"
                  type="text"
                  v-model="addVenue.Name"
                  class="form-control"
                  required
                  placeholder="Enter Name"
                />
              </div>
              <div class="mb-3">
                <label for="form-capacity-input" class="form-label">Capacity:</label>
                <input
                  id="form-capacity-input"
                  type="text"
                  v-model="addVenue.Capacity"
                  class="form-control"
                  required
                  placeholder="Enter Capacity"
                />
              </div>
              <div class="mb-3">
                <label for="form-place-input" class="form-label">Place:</label>
                <input
                  id="form-place-input"
                  type="text"
                  v-model="addVenue.Place"
                  class="form-control"
                  required
                  placeholder="Enter Place"
                />
              </div>
              <div class="mb-3">
                <label for="form-imgURL-input" class="form-label">imgURL:</label>
                <input
                  id="form-imgURL-input"
                  type="text"
                  v-model="addVenue.imgURL"
                  class="form-control"
                  placeholder="Enter imgURL"
                />
              </div>
              <!-- Modal footer with Save and Close buttons -->
              <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                <button type="submit" class="btn btn-primary" data-bs-dismiss="modal">Save Venue</button>
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
      return {
        username:'',
        venues: [],
        addVenue: {
          ID: '',
          Name: '',
          Capacity: '',
          Place: '',
          imgURL:'',
        },
        showMessage: false,
        message: '',  
        VenueID: '',      
      };
    },
    methods: {
      venInit(venue){
        console.log(venue)
        this.addVenue.ID = venue.ID
        this.addVenue.Name = venue.name;
        this.addVenue.Place = venue.place;
        this.addVenue.Capacity = venue.capacity;
        this.addVenue.imgURL = venue.imgURL;
      },

      initForm() {
        this.addVenue.Name = '';
        this.addVenue.Place = '';
        this.addVenue.Capacity = '';
        this.addVenue.imgURL = '';
      }, 

      editVen(){
        const payload = {
          Name: this.addVenue.Name,
          Capacity: this.addVenue.Capacity,
          Place: this.addVenue.Place,
          imgURL: this.addVenue.imgURL,
        };
        console.log(this.addVenue.Name)
        const path = `http://localhost:5000/admin/editV/${this.addVenue.ID}`;
        axios.put(path, payload)
          .then(() => {
            this.message = 'Venue edited!';
            this.showMessage = true;
            this.getVenue();
    
          })
          .catch((error) => {
            console.log(error);
            this.getVenue();
          });
      },

      
      addV(payload) {
      const path = 'http://localhost:5000/admin/addvenue';
      axios.post(path, payload, { headers: {
             Authorization: localStorage.getItem('access_token')
          }})
        .then(() => {
          this.message = 'Venue added!';
          this.showMessage = true;
          this.getVenue();
  
        })
        .catch((error) => {
          console.log(error);
          this.getVenue();
        });
      },


      getVenue(){
        axios.get("http://127.0.0.1:5000/admin/home")
        .then(response => {
          this.venues = response.data;
          
        })
        .catch(error => {
          console.error('Error fetching venues:', error);
        });
      },


      addVen() {
        const payload = {
          Name: this.addVenue.Name,
          Capacity: this.addVenue.Capacity,
          Place: this.addVenue.Place,
          imgURL: this.addVenue.imgURL,
        };
        console.log(this.addVenue['Name'])
        this.addV(payload);
        this.initForm();
      },

      deleteVenue(venue) {
        if (confirm(`Are you sure you want to delete '${venue.name}' venue?`)) {
          console.log(venue.ID)
          const path = `http://localhost:5000/admin/deletevenue/${venue.ID}`;
          
          axios.delete(path,{ headers: {
             Authorization: localStorage.getItem('access_token')
          }})
            .then(() => {
              this.message = 'Venue deleted!';
              this.showMessage = true;
              this.getVenue();
            })
            .catch((error) => {
              console.log(error);
              this.getVenue();
            });
        }
      },


    },
    mounted() {
      const username = this.$route.params.username
      this.username = username
      console.log(username)
      axios.get("http://127.0.0.1:5000/admin/home")
        .then(response => {
          this.venues = response.data;
        })
        .catch(error => {
          console.error('Error fetching venues:', error);
        });
    },
  };
  </script>
  
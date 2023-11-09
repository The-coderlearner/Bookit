<template>
    <div class="adminHome">
      <navBar></navBar>
  
      <section class="container my-5">
      <h1 class="text-center mb-4">Available Shows in {{ venue.Name }}</h1>
      <div class="row justify-content-center">
        <b-alert variant="success" v-if="showMessage" show>{{ message }}</b-alert>

        <!-- Venue Cards -->
        <div v-for="show in shows" :key="show.ID" class="col-md-4 mb-4">
          <div class="card">
            <img :src="show.imgURL || 'https://via.placeholder.com/350x200'" class="card-img-top" alt="Show Image">
            <div class="card-body">
              <h5 class="card-title">{{ show.name }}</h5>
              <h5 class="card-text">{{ show.Ratings }}</h5>
              <p class="card-text">{{ show.Description }}</p>


              <div class="d-flex justify-content-between">
                <button @click.prevent="showInit(show)" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#editShowModal">Edit Show</button>
                <button @click.prevent="deleteShow(show)" class="btn btn-primary">Delete Show</button>
                
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
              <button @click.prevent = "addSh()" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#addShowModal">
                  Add Show
                </button>
            </div>
          </div>
        </div>
        <!-- End Add Venue Button -->
      </div>
    </section>
    <!--    
    //End Available Venues Section 
        //  Modal -->
      <div class="modal fade" id="addShowModal" tabindex="-1" aria-labelledby="addShowModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="addShowModalLabel">Add a new Show</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            
            <form @submit.prevent="addSh">
              <div class="mb-3">

                <label for="form-title-input" class="form-label">Title:</label>
                <input
                  id="form-title-input"
                  type="text"
                  v-model="addShow.name"
                  class="form-control"
                  required
                  placeholder="Enter Name"
                />
              </div>
              <div class="mb-3">
                <label for="form-Description-input" class="form-label">Description:</label>
                <input
                  id="form-Description-input"
                  type="text"
                  v-model="addShow.Description"
                  class="form-control"
                  required
                  placeholder="Enter Description"
                />
              </div>
              <div class="mb-3">
                <label for="form-AvailableSeats-input" class="form-label">Available Seats:</label>
                <input
                  id="form-AvailableSeats-input"
                  type="text"
                  v-model="addShow.Capacity"
                  class="form-control"
                  required
                  placeholder="Enter No. of Seats"
                />
              </div>
              <div class="mb-3">
                <label for="form-Price-input" class="form-label">Price of a seat:</label>
                <input
                  id="form-Price-input"
                  type="text"
                  v-model="addShow.pos"
                  class="form-control"
                  required
                  placeholder="Enter Price per seat"
                />
              </div>
              <div class="mb-3">
                <label for="form-Tag-input" class="form-label">Tag:</label>
                <input
                  id="form-Tag-input"
                  type="text"
                  v-model="addShow.tags"
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
                  v-model="addShow.imgURL"
                  class="form-control"
                  required
                  placeholder="Enter imgURL"
                />
              </div>
              <div class="mb-3">
                <label for="form-Ratings-input" class="form-label">Ratings:</label>
                <input
                  id="form-Ratings-input"
                  type="text"
                  v-model="addShow.Ratings"
                  class="form-control"
                  required
                  placeholder="Enter Ratings"
                />
              </div>
              <div class="mb-3">
                <label for="form-Dates-input" class="form-label">Date</label>
                <input 
                  id="form-Dates-input"
                  type="datetime-local" 
                  class="form-control"
                  v-model="addShow.Dates" 
                  required
                />
              </div>
              
              <!--Modal footer with Save and Close buttons -->
              <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                <button type="submit" class="btn btn-primary" data-bs-dismiss="modal">Save Show</button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>


     <!--Modal Edit--> 
     <div class="modal fade" id="editShowModal" tabindex="-1" aria-labelledby="editShowModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="editShowModalLabel">Edit Show</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <form @submit.prevent="editShow">
              <div class="mb-3">
                <label for="form-title-input" class="form-label">Title:</label>
                <input
                  id="form-title-input"
                  type="text"
                  v-model="addShow.name"
                  class="form-control"
                  required
                  placeholder="Enter Name"
                />
              </div>
              <div class="mb-3">
                <label for="form-Description-input" class="form-label">Description:</label>
                <input
                  id="form-Description-input"
                  type="text"
                  v-model="addShow.Description"
                  class="form-control"
                  required
                  placeholder="Enter Description"
                />
              </div>
              <div class="mb-3">
                <label for="form-AvailableSeats-input" class="form-label">Available Seats:</label>
                <input
                  id="form-AvailableSeats-input"
                  type="text"
                  v-model="addShow.Capacity"
                  class="form-control"
                  required
                  placeholder="Enter No. of Seats"
                />
              </div>
              <div class="mb-3">
                <label for="form-Price-input" class="form-label">Price of a seat:</label>
                <input
                  id="form-Price-input"
                  type="text"
                  v-model="addShow.pos"
                  class="form-control"
                  required
                  placeholder="Enter Price per seat"
                />
              </div>
              <div class="mb-3">
                <label for="form-Tag-input" class="form-label">Tag:</label>
                <input
                  id="form-Tag-input"
                  type="text"
                  v-model="addShow.tags"
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
                  v-model="addShow.imgURL"
                  class="form-control"
                  required
                  placeholder="Enter imgURL"
                />
              </div>
              <div class="mb-3">
                <label for="form-Ratings-input" class="form-label">Ratings:</label>
                <input
                  id="form-Ratings-input"
                  type="text"
                  v-model="addShow.Ratings"
                  class="form-control"
                  required
                  placeholder="Enter Ratings"
                />
              </div>
              <div class="mb-3">
                <label for="form-Dates-input" class="form-label">Date</label>
                <input 
                  id="form-Dates-input"
                  type="datetime-local" 
                  class="form-control"
                  v-model="addShow.Dates" 
                  required
                />
              </div>
              
              <!--Modal footer with Save and Close buttons -->
              <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                <button type="submit" class="btn btn-primary" data-bs-dismiss="modal">Save Show</button>
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
        venue: {
          ID:'',
          Name:'',
          Place: '',
          Capacity: '',
        },
        shows: [],
        addShow: {
          ID: '',
          name: '',
          Capacity: '',
          imgURL:'',
          Description:'',
          pos:'',
          tags:'',
          Dates:'',
          Allseats:'',
          Ratings: '',
          venueID:'',
        },
        showMessage: false,
        message: '',   
      };
    },
    methods: {
      showInit(show){
        
        this.addShow.name = show.name;
        this.addShow.Capacity = show.Capacity;
        this.addShow.imgURL = show.imgURL;
        this.addShow.Description = show.Description;
        this.addShow.pos = show.pos;
        this.addShow.tags = show.tags;
        this.addShow.Dates = show.Date;
        this.addShow.Ratings = show.Ratings;
        console.log(this.addShow);

      },

      initForm() {
        this.addShow.name = '';
        this.addShow.Place = '';
        this.addShow.Capacity = '';
        this.addShow.imgURL = '';
        this.addShow.Description = '';
        this.addShow.pos = '';
        this.addShow.tags = '';
        this.addShow.Dates = '';
        this.addShow.Ratings = '';
      }, 

      editShow(){
        console.log("Helloooo")
        const payload = {
          Name: this.addShow.name,
          Capacity: this.addShow.Capacity,
          Description: this.addShow.Description,
          imgURL: this.addShow.imgURL,
          pos: this.addShow.pos,
          tage: this.addShow.tags,
          Dates: this.addShow.Dates,
          Ratings: this.addShow.Ratings

        };
        console.log("showname =", this.addShow.name)
        const path = `http://localhost:5000/admin/editS/${this.venue.ID}/${this.addShow.name}`;
        console.log(payload)
        axios.put(path, payload)
          .then(() => {
            this.message = 'Show edited!';
            this.showMessage = true;
            this.getShow();
    
          })
          .catch((error) => {
            console.log(error);
            this.getShow();
          });
      },

      
      addS(payload) {
      axios.post(`http://127.0.0.1:5000/admin/${this.addShow.venueID}`, payload,
      { headers: {
             Authorization: localStorage.getItem('access_token')
          }})
        .then(() => {
          this.message = 'Show added!';
          this.showMessage = true;
          this.getShow();
        })
        .catch((error) => {
          console.log(error);
          this.getShow();
        });
      },


      getShow(){
        axios.get(`http://127.0.0.1:5000/admin/${this.venue.ID}`,
        { headers: {
             Authorization: localStorage.getItem('access_token')
          }})
        .then(response => {
          this.venue = response.data.venue;
          console.log(this.venue);
          this.shows = response.data.shows;
        })
        .catch(error => {
          console.error('Error fetching venues:', error);
        });
    },


      addSh() {
        const payload = {
          Name : this.addShow.name,
          Capacity : this.addShow.Capacity ,
          imgURL : this.addShow.imgURL,
          Description : this.addShow.Description,
          pos : this.addShow.pos,
          Tags : this.addShow.tags,
          Dates : this.addShow.Dates ,
          Ratings : this.addShow.Ratings ,
          venue_id:this.addShow.venueID,

        };
        console.log(payload)
        this.addS(payload);
        this.initForm();
      },

      deleteShow(show) {
        if (confirm(`Are you sure you want to delete '${show.name}' from '${this.venue.Name}?`)) {
          //console.log(venue.ID)
          const path = `http://localhost:5000/admin/deleteshow/${this.venue.ID}/${show.ID}`;
          axios.delete(path,{ headers: {
             Authorization: localStorage.getItem('access_token')
          }})
            .then(() => {
              this.message = 'Show deleted!';
              this.showMessage = true;
              this.getShow();
            })
            .catch((error) => {
              console.log(error);
              this.getShow();
            });
        }
      },


    },
    mounted() {
      const username = this.$route.params.username
      const venueID = this.$route.params.venueID
      this.username = username
      console.log("venueID = ",venueID)
      axios.get(`http://127.0.0.1:5000/admin/${venueID}`,{ headers: {
             Authorization: localStorage.getItem('access_token')
          }})
        .then(response => {
          this.venue = response.data.venue;
          console.log(this.venue);
          this.shows = response.data.shows;
          this.addShow.venueID = this.venue.ID

        })
        .catch(error => {
          console.error('Error fetching venues:', error);
        });
    },
  };
  </script>
  
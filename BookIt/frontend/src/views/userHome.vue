<template>
<div class = "userHome">
    <section>
      <navbarUser></navbarUser>
      <div class="row justify-content-center">
        <form method="post" action="showbook.html">
          <div class="container my-5">
            <h1 class="text-center mb-4">Venue</h1>
            <div class="row justify-content-center">
              <div v-for="v in venues" :key="v.ID" class="card">
                <p></p>
                <h3 class="text-center mb-1">{{ v.name }}</h3>
                <hr>
                <div class="row">
                  <div class="col-md-12">
                    <div class="row">
                      <div
                        v-for="show in shows.filter(s => s.venue_id === v.ID)"
                        :key="show.ID"
                        class="col-md-4 mb-4"
                      >
                        <div class="card">
                          <div class="card">
                                                        <div class="card-body">
                            <template v-if="show.Allseats > 0">
                              <div class="img__container">

                              <img :src="show.imgURL" class="card-img-top" alt="Show Image" >
                                <div class="img__overlay">

                                  <p class="img__description">{{ show.Description }}</p>
                                </div>
                              </div>
                            </template>
                            <template v-else>
                              <div class="img__container">
                                <img :src="show.imgURL" style="-webkit-filter: grayscale(100%); filter: grayscale(100%);" class="card-img-top" alt="Show Image" />
                                <div class="img__overlay">
                                <p class="img__description">{{ show.Description }}</p>
                                </div>

                              </div>
                                <div class="card-body">
                                <h5 class="card-title">{{ show.Name }}</h5>
                                <p>Genre: {{ show.tags }}</p>
                                <p>Housefull</p>
                                </div>
                            </template>
                            <h5 class="card-title">{{ show.Name }}</h5>
                            <p>Genre: {{ show.tags}}</p>
                            <a :href="'/' + username + '/home/'  + show.ID" class="btn btn-primary">
                                Book
                            </a>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </form>
      </div>
    </section>
</div>
  </template>
  
  <script>
  import axios from 'axios'

  export default {
    name: 'userHome',
    data() {
      return {
        username: '', // Set your username data here
        venues: [], // Set your venue data here
        shows: [], // Set your show data here
      };
    },
    mounted() {
      const username = this.$route.params.username
      this.username = username
      console.log(username)
      axios.get("http://127.0.0.1:5000/")
        .then(response => {
          this.venues = response.data.venues;
          this.shows = response.data.shows;
          console.log(response.data.venues)
        })
        .catch(error => {
          console.error('Error fetching venues:', error);
        });
    },
  };
  </script>
  
  <style>
 .img__container {
    position: relative;
  }

  .img__overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%; /* Adjust the height to cover the entire card */
    background: rgba(0, 0, 0, 0.6);
    color: white;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    opacity: 0;
    transition: opacity 0.25s;
  }

  .img__description {
    font-size: smaller;
    align-items: center;
    align-self: center;
    justify-content: center;
  }

  .img__overlay > * {
    transform: translateY(15px);
    transition: transform 0.25s;
  }

  .img__container:hover .img__overlay {
    opacity: 1;
  }
</style>

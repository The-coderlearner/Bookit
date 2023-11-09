<template>
    <div class="adminProfile">
        <navBar></navBar>
    <div class="container-fluid">
      <div class="row">
        <div class="col-15 text-center">
          <h1>{{ username }}</h1>
        </div>
      </div>
      <p></p>
      <div class="container mt-5">
    <div class="row justify-content-center">
      <div class="col-md-8">
        <h2>Venues List</h2>
        <ul class="list-group">
          <li
            v-for="(venue) in venues"
            :key="venue.ID"
            class="list-group-item d-flex justify-content-between align-items-center"
          >
            {{ venue.Name }}
            <button
              class="btn btn-primary"
              @click="downloadSummary(venue.ID, venue.Name)"
            >
              Download Summary
            </button>
          </li>
        </ul>
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
            venues: [],
            venueName:'',
          }
        
      },
      methods: {
            async downloadSummary(venueID, venueName) {
            try {
                this.venueName = venueName;
                const response = await axios.get(`http://127.0.0.1:5000/generate_csv/${venueID}`, {
                responseType: 'blob',
                });
                const blob = new Blob([response.data], { type: 'text/csv' });
                const url = window.URL.createObjectURL(blob);
                const link = document.createElement('a');
                link.href = url;
                link.download = `${venueName}_summary.csv`;
                link.style.display = 'none';
                document.body.appendChild(link);
                link.click();
                document.body.removeChild(link);
                window.URL.revokeObjectURL(url);
            } catch (error) {
                console.error('Error downloading CSV:', error);
            }
            },

      },
  
      mounted() {
        const username = this.$route.params.username
      this.username = username
      console.log(username)
      axios.get('http://127.0.0.1:5000/admin/summary')
        .then(response => {
          this.venues = response.data.venues;
          console.log(response.data.venues)
        })
        .catch(error => {
          console.error('Error fetching venues:', error);
        });
    },
     
    };
</script>
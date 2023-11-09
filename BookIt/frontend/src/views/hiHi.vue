<template>
    <div class="hiHi">
     
  <div class="centered-container">
    <h1>Welcome to BookIt</h1>
    <div class="button-container">
      <router-link to="/login">
        <button class="btn btn-outline-success" style="margin-right: 10px;" >Go to Login</button>
      </router-link>

      <router-link to="/admin">
        <button class="btn btn-outline-danger" style="margin-left: 10px;" id="color">Go to Admin</button>
      </router-link>
    </div>
  </div>
</div>
</template>


<script>
export default{
    name: "hiHi",
    mounted(){
        localStorage.setItem('access_token', '');
        localStorage.setItem('id', '');
        localStorage.setItem('name', '');
    }


}

</script>

<style scoped>
.centered-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  text-align: center;
}

.button-container {
  margin-top: 20px; /* Adjust the margin as needed for spacing */
}

/* Add any additional styles as needed */
</style>

    

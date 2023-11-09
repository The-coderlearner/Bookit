<template>
  <div class="adminLogin">
    <section class="gradient-form">
      <div class="container py-2 h-100">
        <div class="row d-flex justify-content-center align-items-center h-100">
          <div class="col-xl-10">
            <div class="card rounded-3 text-black">
              <div class="row g-0">
                <div class="col-lg-6">
                  <div class="card-body p-md-2 mx-md-5">
                    <div class="text-center">
                      <img
                        src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-login-form/lotus.webp"
                        style="width: 185px;"
                        alt="logo"
                      />
                      <h4 class="mt-1 mb-5 pb-1">Welcome to BookIt</h4>
                    </div>
                    <form>
                      <div class="form-outline mb-4">
                        <label class="form-label" for="username">Username</label>
                        <input
                          type="text"
                          id="username"
                          v-model="data.username"
                          class="form-control"
                          placeholder="Enter your Username"
                        />
                      </div>
                      <div class="form-outline mb-4">
                        <label class="form-label" for="password">Password</label>
                        <input
                          type="password"
                          id="password"
                          v-model="data.password"
                          class="form-control"
                        />
                      </div>
                      <div class="text-center pt-1 mb-4 pb-10">
                        <div class="button-container">
                          <button class="btn btn-primary" type="submit" @click.prevent="onLogin">Login</button>
                          <button class="btn btn-primary" type="button" @click="clear">Clear</button>
                        </div>
                        <p></p>
                        User? <router-link to="/login"><button class="btn btn-primary">click here</button></router-link>
                      </div>
                      <div class="d-flex align-items-center justify-content-center pb-4">
                        <p class="mb-0 me-2">Adding a new account?</p>
                        <router-link to="/adminsignup"><button class="btn btn-outline-danger">Create new</button></router-link>
                      </div>
                    </form>
                  </div>
                </div>
                <div class="col-lg-6 d-flex align-items-center gradient-custom-2">
                  <div class="text-white px-3 py-4 p-md-5 mx-md-4">
                    <h4 class="mb-4">We are more than just a company</h4>
                    <p class="small mb-0">Book any show you want easily! :D</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import axios from 'axios';
import { useRouter } from 'vue-router';
import { ref } from 'vue';

export default {
  name: 'logIn',
  setup() {
    const router = useRouter();
    const data = ref({
      username: '',
      password: '',
    });

    const onLogin = async () => {
      console.log(data.value.username);
  
      try {
        const response = await axios.post('http://127.0.0.1:5000/adminlogin', 
                                          data.value, 
                                          {headers: {'Content-Type': 'application/json'}});
        const responseData = response.data;
        console.log("response data = ",responseData);
        localStorage.setItem('access_token', responseData.token);
        localStorage.setItem('id', responseData.id);
        localStorage.setItem('user_type', responseData.userType);
        console.log( localStorage['access_token'])
        router.push({ name: 'adminHome',params:{ username: data.value.username }});
      } catch (error) {
        console.error(error);
        router.push({ name: 'adminLogin' });
        (data.value.username = '');
        (data.value.password = '');
        alert('Wrong Username or Password, Please try again');
      }
    };
  
    const clear = async () => {
      data.value.username = '';
      data.value.password = '';
    };

    return {
      data,
      onLogin,
      clear,
    };
  },
};
</script>


<style scoped>
    .button-container button {
      margin-right: 10px;
    }
    .gradient-form{
      background: #FAF9F6; 
     }
   .gradient-custom-2 {
        background: #fccb90;
        background: -webkit-linear-gradient(to right, #ee7724, #d8363a, #dd3675, #b44593);
        background: linear-gradient(to right, #ee7724, #d8363a, #dd3675, #b44593);
    }
   
    @media (min-width: 768px) {
            .gradient-form {
            height: 100vh !important;
    }
    }
    @media (min-width: 769px) {
        .gradient-custom-2 {
        border-top-right-radius: .3rem;
        border-bottom-right-radius: .3rem;
    }
    }
h3 {
margin: 40px 0 0;
}
ul {
list-style-type: none;
padding: 0;
}
li {
display: inline-block;
margin: 0 10px;
}
a {
color: #42b983;
}
</style>
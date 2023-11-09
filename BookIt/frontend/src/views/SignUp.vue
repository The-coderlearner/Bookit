<template>
    <div class="SignUp">
    <section class=" gradient-form">
   <div class="container py-2 h-100">
     <div class="row d-flex justify-content-center align-items-center h-100">
       <div class="col-xl-10">
         <div class="card rounded-3 text-black">
           <div class="row g-0">
             <div class="col-lg-6">
               <div class="card-body p-md-1 mx-md-5">
 

                 <div class="text-center">
                   <img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-login-form/lotus.webp"
                     style="width: 185px;" alt="logo">
                    
                 </div>
 
                 <form method="POST" >
                   
                   
                   
                   <div class="form-outline mb-4">
                       <label class="form-label" for="form2Example11">Name</label>
                       <input v-model="data.name" name = "name" class="form-control"
                         placeholder="Name" />
                   
                         
                     </div>
                     <div class="form-outline mb-4">
                       <label class="form-label" for="form2Example11">Username</label>
                       <input v-model="data.username" name = "username" class="form-control"
                         placeholder="Username" />
                       
                     </div>
                     <div class="form-outline mb-4">
                       <label class="form-label" for="form2Example11">E-Mail</label>
                       <input v-model="data.email" type="email" name = "email" class="form-control"
                         placeholder="E-Mail" />
                       
                     </div>
                   <div class="form-outline mb-2">
                     <label class="form-label" for="form2Example22">Password</label>
                     <input v-model="data.password" type="password" name="password" class="form-control" />
                     
                   </div>
 
                   <div class="text-center pt-1 mb-3 pb-1">
                     <input type="hidden" name="next" >
                     <button class="btn btn-primary" @click.prevent=createAcc>Sign-up</button> 
                   </div>
 
                   <div class="d-flex align-items-center justify-content-center pb-4">
                     <p class="mb-0 me-2">Already have an account?</p>
                     <button class="btn btn-primary" @click=onLogin>Log In</button>
                   </div>
 
                 </form>
 
               </div>
             </div>
             <div class="col-lg-6 d-flex align-items-center gradient-custom-2">
               <div class="text-white px-3 py-4 p-md-5 mx-md-4">
                 <h4 class="mb-4">Welcome to BookIt, We are more than just a company!</h4>
                 <p class="small mb-0">Book any show you want easily! :D</p>
               </div>
             </div>
           </div>
         </div>
       </div>
     </div>
   </div>
 </section></div>
</template>

<script>
import axios from 'axios';
import { useRouter } from 'vue-router';
import { ref } from 'vue';

export default {
 name: 'SignUp',
 setup(){
     const router = useRouter();
     const data = ref({
       username: '',
       password: '',
       email: '',
       name: '',
     });
     var response = null
     const createAcc = async () => {
            try{
              console.log(data.value);
              response = await axios.post('http://127.0.0.1:5000/signup',
                                                data.value, 
                                                {headers: {'Content-Type': 'application/json'}}
                                                )
              console.log(response)
              router.push({ name: 'logIn' });
            }
            catch(error){
              console.log(error)
              await router.push('/signup');
              data.value.username=''
              data.value.name=''
              data.value.password=''
              data.value.email=''
              alert('Sorry! Already Exists');
            }
    }
    const onLogin = async () => {
      await router.push('/login');
    };
    return {
      data,
      onLogin,
      createAcc
    };
  
 },
};

</script>

<style scoped>
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
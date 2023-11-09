import { createRouter, createWebHistory } from 'vue-router';
import logIn from '../views/logIn.vue'
import SignUp from '../views/SignUp.vue'
import userHome from '../views/userHome.vue'
import adminLogin from '../views/adminLogin.vue'
import adminSignup from '../views/adminSignup.vue'
import adminHome from '../views/adminHome.vue'
import adminShow from '../views/adminShow.vue'
import hiHi from '../views/hiHi.vue'
import bookShow from '../views/bookShow.vue'
import searchResult from '../views/searchResult.vue'
import userVenueShow from '../views/userVenueShow.vue'
import userProfile from  '../views/userProfile.vue'
import adminProfile from '../views/adminProfile.vue'

const routes = [
    {
        path:'/:username/home/:showid',
        name:'bookShow',
        component: bookShow,
        meta: {requiresAuth: true}

    },
    {
        path:'/:username/profile/view/summary',
        name: 'adminProfile',
        component: adminProfile,
        meta: { requiresAuth: true,requiresAdmin: true  }
    },
    
    {
        path:'/:username/venue/:venueid',
        name:'userVenueShow',
        component: userVenueShow,
        meta: {requiresAuth: true}

    },
    {
        path:'/:username/searchresult/:sv',
        name:'searchResult',
        component: searchResult,
        meta: { requiresAuth: true }
    },

    {
        path: '/',
        name: 'hiHi',
        component: hiHi,
    },
    {
        path: '/login',
        name: 'logIn',
        component: logIn,
    },
    {
        path: '/admin',
        name: 'adminLogin',
        component: adminLogin,

    },
    {
        path: '/adminsignup',
        name: 'adminSignup',
        component: adminSignup,
    },

    {
        path: '/:username',
        name: 'userProfile',
        component: userProfile,
        meta: { requiresAuth: true }
    },
    {

        path: '/:username/home',
        name: 'userHome',
        component: userHome,
        meta: {requiresAuth: true}
    },
    {
        path: '/signup',
        name: 'SignUp',
        component: SignUp,
    },
    {
        path: '/admin/:username',
        name: 'adminHome',
        component: adminHome,
        meta: { requiresAuth: true, requiresAdmin: true }

    },
    {
        path: '/admin/:username/:venueID',
        name: 'adminShow',
        component: adminShow,
        meta: { requiresAuth: true, requiresAdmin: true }

    }

]
const router = createRouter({
    history: createWebHistory(),
    routes,
  });
  
export default router;
import jwt_decode from "jwt-decode";
function verifyToken(token){
    try{
        const decodedToken = jwt_decode(token);
        return decodedToken
    }catch(error){
        console.error(error)
        return null
    }
}
router.beforeEach((to, from, next)=> {
    const isAuthenticated = localStorage['access_token']
    const isAdmin = localStorage['user_type'] === 'admin'
    console.log(isAuthenticated)
    if(to.matched.some(record => record.meta.requiresAuth)){
        if(isAuthenticated === ''){
            alert('Please Login to continue')
            next({path: '/'})
        }else{
            try{
                
                const decodedToken = verifyToken(isAuthenticated)
                if(decodedToken){
                    if(to.matched.some(record => record.meta.requiresAdmin)&& (!isAdmin)){
                        alert('Not an Admin - Access Denied!')
                        next({path: '/login'})
                    }else{
                        console.log(decodedToken)
                        next()
                    }
                }else{
                    alert('Session expired!!')
                    next({path: '/login'})
                }
            }catch(error){
                console.error(error)
                next({path: '/'})
            }
        }
    }else{
        next()
    }
})
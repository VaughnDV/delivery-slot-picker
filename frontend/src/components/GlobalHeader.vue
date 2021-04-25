<template>
  <div id="header">
    <b-navbar type="dark" variant="dark">
      <a class="navbar-brand" href="/">First App</a>
      <b-navbar-nav class="ml-auto" v-if="$route.meta.requiresAuth">
        <b-nav-item-dropdown right v-if="isLoggedIn">
          <template slot="button-content">{{ fullName }}</template>
          <b-dropdown-item href="#" @click="clickLogout">Logout</b-dropdown-item>
        </b-nav-item-dropdown>
        <b-nav-item href="#" @click="clickLogin" v-else>Login</b-nav-item>
      </b-navbar-nav>
    </b-navbar>
  </div>
</template>

<script>
  export default {
    computed: {
      fullName: function () {
        return this.$store.getters['auth/fullName']
      },
      isLoggedIn: function () {
        return this.$store.getters['auth/isLoggedIn']
      }
    },
    methods: {
      clickLogout: function () {
        this.$store.dispatch('auth/logout')
        this.$store.dispatch('message/setInfoMessage', { message: 'Logging out' })
        this.$router.replace('/login')
      },
      clickLogin: function () {
        this.$store.dispatch('message/clearMessages')
        this.$router.replace('/login')
      }
    }
  }
</script>

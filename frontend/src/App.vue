<template lang="html">
  <div>
    <div id="nav">
      <router-link to="/">User</router-link>
       | <router-link :to="{ name: 'pick-slots' }">Delivery Slots</router-link>
      | <router-link :to="{ name: 'register' }">Register</router-link>
    </div>

    <router-view/>
  </div>
</template>

<script>

export default {
  name: 'App',
  components: {

  }
}
</script>

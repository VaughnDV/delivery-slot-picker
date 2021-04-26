<template>
  <div class="container">
    <div class="my-5 py-5">
      <div class = "col-lg-8" v-if = "count">
        <div class = "col-12">
          <h1>Pick delivery dates</h1>
        </div>
      </div>
      <div class = "col-lg-8" v-if = "count">
        <div class = "col-12">
          <div class="card h-100" v-for="slot in results">
            <div class="card-body">
              <div class="card-title">
                <h4>{{ slot.name }} of {{ slot.date }}</h4>
              </div>
              <p>From {{ slot.start_time }} to {{ slot.end_time }}</p>
            </div>
            </div>
          </div>
        </div>
      </div>
  </div>
</template>

<script>

export default {
  name: 'ViewDeliverySlots',
  // { "id": 1, "name": "morning", "date": "2021-04-24", "start_time": "07:00:00", "end_time": "12:00:00", "special_item": true, "available": true }
  data () {
    return {
      'count': null,
      'next': null,
      'previous': null,
      'results': null
    }
  },
  created () {
    this.$store.dispatch('getDeliverySlots', this.$route.params.id)
      .then(data => {
        console.log(data)
        this.count = data['count']
        this.results = data['results']
      })
      .catch(error => {
        console.log(error)
      })
  }
}
</script>

<style>
</style>

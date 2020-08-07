<template>
  <v-app>
    <div class="containers">
      <v-row style="width:100%">
        <v-col cols="12" style="display:flex;justify-content:center">
          <h1>TIME TABLE SYSTEM</h1>
        </v-col>
        <v-col cols="12">
          <AddForm :time="time" :day="day" @add="add" @del="del"/>
        </v-col>
        <v-col cols="12">
          <Table :time="time" :day="day" :subject="subject"/>
        </v-col>
      </v-row>
    </div>
  </v-app>
</template>

<script>
import axios from 'axios'
import AddForm from './components/addform'
import Table from './components/table'
export default {
  components: {
    AddForm,
    Table,
  },
  data() {
    return {
      time: [
        '08.00',
        '08.30',
        '09.00',
        '09.30',
        '10.00',
        '10.30',
        '11.00',
        '11.30',
        '12.00',
        '12.30',
        '13.00',
        '13.30',
        '14.00',
        '14.30',
        '15.00',
        '15.30',
        '16.00',
        '16.30',
        '17.00',
        '17.30',
        '18.00',
        '18.30',
        '19.00',
        '19.30',
        '20.00',
        '20.30',
        '21.00',
      ],
      day: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
      subject: [],
    }
  },
  methods:{
    add(val){
      axios.post('http://localhost:8000/subject/',val).then(res=>{
        this.subject = res.data
      })
    },
    del(){
      axios.post('http://localhost:8000/subject/clear').then(res=>{
        this.subject = res.data
      })
    }
  },
  async mounted() {
      axios.get('http://localhost:8000/subject/').then(res=>{
        this.subject = res.data
      })
  }
}
</script>

<style>
.containers {
  width: 100vw;
  padding: 2%;
  margin: 0;
  display: flex;
  justify-content: center;
}
</style>

<template>
  <v-row class="form">
    <v-col cols="11">
      <v-row>
        <v-col cols="4">
          <v-text-field v-model="info.subject_code" label="Subject Code" :rules="[v=>v.length <= 6||'Subject Code must less than 7 characters']"/>
        </v-col>
        <v-col cols="4">
          <v-text-field v-model="info.subject_name" label="Subject Name" :rules="[v=>v.length <= 50||'Subject Name must less than 51 characters']"/>
        </v-col>
        <v-col cols="4">
          <v-text-field v-model="info.lecturer" label="Lecturer" :rules="[v=>v.length <= 50||'Lecturer must less than 51 characters']" />
        </v-col>
        <v-col cols="3">
          <v-text-field v-model="info.room" label="Room" :rules="[v=>v.length <= 11||'Room must less than 11 characters']"/>
        </v-col>
        <v-col cols="3">
          <v-select v-model="info.day" label="Day" :items="day" :rules="[v=>v.length == 3||'Day must be 3 characters']"/>
        </v-col>
        <v-col cols="3">
          <v-select v-model="info.starttime" label="Start Time" :items="time" :rules="[v=>v.length == 5||'Day must be 5 characters']"/>
        </v-col>
        <v-col cols="3">
          <v-select v-model="info.endtime" label="End Time" :items="time" :rules="[v=>v.length == 5||'Day must be 5 characters']"/>
        </v-col>
      </v-row>
    </v-col>
    <v-col cols="1" class="addbutton">
      <v-row>
        <v-col cols="12" style="display:flex;align-item:center;justify-content:center">
          <v-btn @click="add">ADD</v-btn>
        </v-col>
        <v-col cols="12" style="display:flex;align-item:center;justify-content:center">
          <v-btn @click="del">CLEAR</v-btn>
        </v-col>
      </v-row>
    </v-col>
  </v-row>
</template>

<script>
export default {
  data() {
    return {
      info: {
        subject_code: '',
        subject_name: '',
        lecturer: '',
        room: '',
        day: '',
        starttime: '',
        endtime: ''
      }
    }
  },
  props: {
    day: Array,
    time: Array
  },
  methods: {
    add() {
      if(this.validate()){
        this.$emit('add', this.info)
        this.info = {
            subject_code: '',
            subject_name: '',
            lecturer: '',
            room: '',
            day: '',
            starttime: '',
            endtime: ''
        }
      }
    },
    del() {
      this.$emit('del')
    },
    getTime(time) {
      let t = time.split('.')
      let h = parseInt(t[0])
      let m = parseInt(t[1])
      return h * 60 + m
    },
    validate() {
      if (
        this.info.subject_code != '' &&
        this.info.subject_code.length <= 6 &&
        this.info.subject_name != '' &&
        this.info.subject_name.length <= 50 &&
        this.info.lecturer != '' &&
        this.info.lecturer.length <= 50 &&
        this.info.room != '' &&
        this.info.room.length <= 10 &&
        this.info.day != '' &&
        this.info.day.length == 3 &&
        this.info.starttime != '' &&
        this.info.starttime.length == 5 &&
        this.info.endtime != '' &&
        this.info.endtime.length == 5
      ) {
          if(this.getTime(this.info.endtime) - this.getTime(this.info.starttime) > 0){
            return true
          } else {
              alert('End time must be after Start time!')
              return false
          }
      } else {
        return false
      }
    }
  }
}
</script>

<style>
.addbutton {
  display: flex;
  align-items: center;
}
</style>

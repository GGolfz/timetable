<template>
  <v-row class="subject" :style="`background:${info.color}`">
      <v-col class="subject_detail" :cols="12">
          {{info.subject_code}}
      </v-col>
      <v-col class="subject_detail" :cols="12">
          {{info.subject_name}}
      </v-col>
      <v-col class="subject_detail" :cols="12">
          {{info.lecturer}}
      </v-col>
      <v-col class="subject_detail" :cols="12">
          {{info.room}}
      </v-col>
  </v-row>
</template>

<script>
export default {
    props:{
        info:Object
    }
}
</script>

<style>
    .subject{
        width:100%;
        text-align: center;
        margin:0;
        height: 100%;
    }
    .subject_detail{
        padding:0;
    }
</style>
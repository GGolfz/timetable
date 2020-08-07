<template>
  <v-row>
      <v-col cols="12">
          <v-row v-for="(r,i) in table" :key="i">
              <v-col v-for="(c,j) in r" :key="j" :style="i==0?j==0?`max-width:${c.width*100/(time.length)}%;
    border-width: 1px;`:`;max-width:${c.width*100/(time.length)}%;border-width: 1px 1px 1px 0px; `:j==0?`max-width:${c.width*100/(time.length)}%;border-width: 0px 1px 1px 1px`:`max-width:${c.width*100/(time.length)}%`" class="sub">
                <Subject style="padding:1px" v-if="c.value.substring(0,3)=='key'" :info="getDetail(c.value)"/>
                <div style="padding:2px" v-else>{{c.value}}</div>
              </v-col>
          </v-row>
      </v-col>
  </v-row>
</template>

<script>
import Subject from './subject'
export default {
    components:{
        Subject
    },
    data(){
        return{
            table:[]
        }
    },
    props:{
        day:Array,
        time:Array,
        subject:Array
    },

    async mounted(){
        await this.generateTable();
    },
    watch: {
        subject() {
            this.generateTable();   
        }
    },
    methods: {
        async getSubject(day,time) {
            for(let s of this.subject){      
                if(s.day==day){
                    let ind = await this.time.findIndex(t=>t == time);
                    let start = await this.time.findIndex(t=>t == s.starttime);
                    let end = await this.time.findIndex(t=> t == s.endtime);
                    if(ind>=start && ind <end){
                        let key = 'key'+s.subject_code+',room'+s.room;
                        return {key:key,width:end-start}
                    }
                }
            }
            return {key:'',width:1}
        },
        getDetail(key){
            let temp =key.split(',')
            let code = temp[0]
            let room = temp[1]
            for(let s of this.subject){
                if(s.subject_code == code.substring(3) && s.room == room.substring(4)){
                    return s
                }
            }
            return {
                subject_code: '',
                subject_name: '',
                lecturer: '',
                room: '',
                day: '',
                starttime: '',
                endtime: '',
                color:''
            }
        },
        async generateTable(){
            this.table = []
            let days = ['',...this.day];
            let times = ['',...this.time];
            for(let i = 0 ;i<days.length;i++){
                let temp = []
                for(let j = 0 ;j<times.length-1;j++){
                    if(j==0){
                        temp.push({value:days[i],width:1});
                    }
                    else if(i==0){
                        temp.push({value:`${times[j]} - ${times[j+1]}`,width:1});
                    }
                    else {
                        let des = await this.getSubject(days[i],times[j]);
                        temp.push({value:des.key,width:des.width})
                        j+=des.width-1;
                    }
                }
                this.table.push(temp);
            }
        }
        
    }
}
</script>

<style>
.sub{
    overflow-wrap:break-word;
    padding:0;
    border-style: solid;
    border-color:#444444;
    border-width: 0px 1px 1px 0px ;
    border-collapse:collapse;
    text-align: center;
    display:flex;
    align-items: center;
    justify-content: center;
}
</style>
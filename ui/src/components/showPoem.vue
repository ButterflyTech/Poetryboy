<template>
  <div class="hello">
    <h1>{{ poem.title }}</h1>
    <h4>{{ poem.dynasty }} - {{poem.author}}</h4>
    <pre class="paragraphs">{{ poem.paragraphs }}</pre>
    <av-waveform v-if="poem_audio_url != null"
                 :audio-src="poem_audio_url"
    ></av-waveform>
    <button class="lucky" v-on:click="lucky_click" v-if="!loading">手气不错</button>
    <vue-loading
            type="bars"
            color="#d9544e"
            :size="{ width: '15px', height: '15px' }"
            v-if="loading"
    >
    </vue-loading>

  </div>
</template>

<script>

    export default {
        name: 'showPoem',
        props: {
            msg: String
        },
        data() {
            return {
                poem: {
                    author: null,
                    dynasty: null,
                    id: null,
                    paragraphs: null,
                    strains: null,
                    title: null
                },
                poem_audio_url: null,
                loading: false
            }
        },
        mounted() {
            this.lucky_click();
        },

        methods: {
            lucky_click: function () {
                this.loading = true;
                this.poem_audio_url = null;
                this.axios.get('/backend/give_me_poem/').then((response)=>{
                    this.poem = response.data;
                    this.poem_audio_url = "/backend/give_me_audio/" + this.poem.id + "/";
                    this.loading = false;
                }).catch((error)=>{
                    alert(error);
                    this.loading = false;
                })
            }
        }


    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
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

  .paragraph {
    max-width: 60%;
  }

  pre {
    text-align:center
  }

  .paragraphs {
    font-size: large;
  }


  .lucky { /* 按钮美化 */
    margin-top: 10px;
    width: 270px; /* 宽度 */
    height: 40px; /* 高度 */
    border-width: 0px; /* 边框宽度 */
    border-radius: 3px; /* 边框半径 */
    background: #1E90FF; /* 背景颜色 */
    cursor: pointer; /* 鼠标移入按钮范围时出现手势 */
    outline: none; /* 不显示轮廓线 */
    font-family: Microsoft YaHei; /* 设置字体 */
    color: white; /* 字体颜色 */
    font-size: 17px; /* 字体大小 */
  }
  .lucky:hover { /* 鼠标移入按钮范围时改变颜色 */
    background: #5599FF;
  }
</style>

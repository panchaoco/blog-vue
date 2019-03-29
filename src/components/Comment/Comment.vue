<template>
  <section class="comment-container">
    <p class="comment-title">有问题可以提问哦</p>
    <input-comment @on-change="inputReply" @submit-comment="submitComment" />
    <div class="comment-content">
      <div class="comment-item" v-for="(item, index) in commentContent" :key="index">
        <div class="first-comment">
          <div class="user-img">
            <img src="./img/default.gif" alt="">
          </div>
          <div class="content">
            <div class="top">{{item.nickname}}</div>
            <div class="time">{{item.comment_time}}</div>
            <div class="comment-p"><span v-html="item.content"></span></div>
            <div class="user-profile" @click="item.isReply = !item.isReply">
              <span class="item-text">回复</span>
            </div>
            <div class="sub-reply" v-if="item.isReply">
              <div class="reply-input">
                <input-comment @on-change="inputReply" @submit-comment="replySubmit(item)" />
              </div>
            </div>
          </div>

        </div>
        <div class="sub-comment-wrapper">
          <div class="sub-comment" v-if="item.children && item.children.length > 0" v-for="(sub_item, sub_index) in item.children">
            <div class="user-img">
              <img src="./img/default.gif" alt="">
            </div>
            <div class="content">
              <div class="top">
                <span class="username">
                  <span>{{sub_item.nickname}}</span>
                  <em class="reply">回复</em>
                  <span  class="parent-username">{{item.nickname}}</span>
                </span>
              </div>
              <div class="time">{{sub_item.comment_time}}</div>
              <p class="comment-p">
                <span v-html="sub_item.content"></span>
              </p>
              <div class="user-profile" @click="sub_item.isReply = !sub_item.isReply">
                <span class="item-text">回复</span>
              </div>
              <div class="sub-reply" v-if="sub_item.isReply">
                <div class="reply-input">
                  <input-comment @on-change="inputReply" @submit-comment="replySubmit(item)" />
                </div>
                <div class="reply-profile">
                  <Icon class="emoji-btn" @click="sub_item.addEmoji = !sub_item.addEmoji"  type="md-happy" />
                  <div class="reply-submit">
                    <Button type="primary" @click="replySubmit(item, sub_item)">提交</Button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
  import emoji from '../../assets/emoji/emoji'
  import BlogEmoji from '../../components/Emoji/Emoji'
  import InputComment from '../InputComment/InputComment'
  export default {
    name: "Comment",
    data() {
      return {
        imgSrc: '',
        icons: [],
        addEmoji: false,
        commentText: '',
        commentContent: [
        ],
        article_id: this.$route.params.id,
        replyContent: '',
        modalConfig: {
          title: '温馨提示',
          content: '你还没有输入评论哦',
          width: 400
        },
        formData: {
          nickname: '',
          email: '',
          content: ''
        },
      }
    },
    created() {
      this.handleEmoji()
      this.getComment()
    },
    methods: {
      handleEmoji() {
        Object.entries(emoji).forEach(([key, val]) => {
          this.icons.push({
            name: val,
            img: require(`../../assets/emoji/emoji_res/${val}.png`),
            text: key
          })
        })
      },
      choiceEmoji(item) {
        this.commentText += item.text;
      },
      reply(item) {
        this.replyContent += item.text;
      },
      getComment() {
        this.$store.dispatch('article/getComment', {
          method: 'GET',
          body: {
            article_id: this.article_id
          }
        }).then(res => {
          this.commentContent = res.data.map(item => {
            const newItem = Object.assign({}, item)
            newItem.isReply = false
            newItem.addEmoji = false
            newItem.placeholder = ''
            newItem.content = analyzeEmoji(newItem.content)
            if (newItem.children && newItem.children.length > 0) {
              newItem.children = newItem.children.map(c => {
                c.addEmoji = false
                c.isReply = false
                c.placeholder = ''
                c.content = analyzeEmoji(c.content)
                return c
              })
            }
            return newItem
          })
        })

        const analyzeEmoji = (cont) => {
          const reg1 = /\[[\u4e00-\u9fa5]+\]/g
          const reg2 = /\[[\u4e00-\u9fa5]+\]/
          const content = cont.match(reg1)
          let str = cont
          let src = ''
          let key = ''
          if (content) {
            for (let i = 0; i < content.length; i++) {
              for (let j = 0; j < this.icons.length; j++) {
                if (this.icons[j].text === content[i]) {
                  src = this.icons[j].img
                  key = this.icons[j].text
                  break
                }
              }
              str = str.replace(reg2, `<img src="${src}" />`)
            }
          }
          return str
        }
      },
      inputReply(formData) {
        this.formData = formData

      },
      submitComment(item = null) {
        // if (!this.commentText) return this.$Modal.warning(this.modalConfig)
        this.$store.dispatch('article/addComment', {
          id: this.article_id,
          comment_type: 1,
          article_id: this.article_id,
          ...this.formData
        }).then(res => {
          if (res.state === 0) {
            this.getComment()
          }
        })
      },
      replySubmit(item) {
        this.modalConfig.content = '你还没有输入回复哦'
        if (!this.formData.content) return this.$Modal.warning(this.modalConfig)
        this.$store.dispatch('article/addComment', {
          id: item.id,
          parent: item.id,
          comment_type: 2,
          ...this.formData
        }).then(res => {
          if (res.state === 0) {
            this.replyContent = ''
            this.getComment()
          }
        })
      },
      firstReply(item) {
        item.isReply = !item.isReply
        item.addEmoji = false
        item.placeholder = `${localStorage.getItem('username')}回复${item.username}`
      }
    },
    components: {
      BlogEmoji,
      InputComment
    }
  }
</script>

<style lang="less" scoped>
  @import "./Comment";
</style>

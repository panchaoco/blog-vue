<template>
  <section class="comment-container">
    <p class="comment-title">有问题可以提问哦</p>
    <div class="input-comment">
      <div class="input-item">
        <Input style="width: 75%" v-model="formData.nickname" placeholder="昵称" />
        <span class="label">昵称（必填）</span>
      </div>
      <div class="input-item">
        <Input style="width: 75%" v-model="formData.nickname" placeholder="邮箱" />
        <span class="label">邮箱（必填）</span>
      </div>
      <div class="input-item">
        <Input type="textarea" style="width: 100%" v-model="commentText" :rows="3" placeholder="输入评论" />
      </div>
      <div class="input-item">
        <Button type="primary">提交评论</Button>
      </div>
    </div>
    <div class="comment-content">
      <div class="comment-item" v-for="(item, index) in commentContent" :key="index">
        <div class="first-comment">
          <div class="user-img">
            <img :src="item.top_img" alt="">
          </div>
          <div class="content">
            <div class="top">
              <span class="username">{{item.username}}</span>
              <span class="time">{{item.comment_time}}</span>
            </div>
            <p>
              <span v-html="item.content"></span>
            </p>
            <div class="user-profile">
              <div class="up profile-item">
                <Icon type="md-thumbs-up" />
                <span class="item-text">赞一下</span>
              </div>
              <div class="reply-wrapper profile-item" @click="firstReply(item)">
                <Icon type="ios-share-alt" />
                <span class="item-text">回复</span>
              </div>
              <div class="down profile-item">
                <Icon type="md-thumbs-down" />
                <span class="item-text">踩一脚</span>
              </div>
            </div>
            <div class="sub-reply" v-if="item.isReply">
              <div class="reply-input">
                <Input :placeholder="item.placeholder" v-model="replyContent" type="textarea" :rows="1" />
                <blog-emoji @choiceEmoji="reply" :visible="item.addEmoji" :height="440" :style="{borderTop: 'none', marginTop: '-1px'}"></blog-emoji>
              </div>
              <div class="reply-profile">
                <!--<img @click="item.addEmoji = !item.addEmoji" class="emoji-btn" src="../../assets/emoji/emoji_res/emoji_24.png" alt="">-->
                <Icon @click="item.addEmoji = !item.addEmoji" class="emoji-btn" type="md-happy" />
                <div class="reply-submit">
                  <Button type="primary" @click="replySubmit(item)">提交</Button>
                </div>
              </div>
            </div>
          </div>

        </div>
        <div class="sub-comment-wrapper">
          <div class="sub-comment" v-if="item.children && item.children.length > 0" v-for="(sub_item, sub_index) in item.children">
            <div class="user-img">
              <img :src="sub_item.top_img" alt="">
            </div>
            <div class="content">
              <div class="top">
                <span class="username">
                  <router-link to="/">{{sub_item.username}}</router-link>
                  <em class="reply">回复</em>
                  <router-link to="/" class="parent-username">{{item.username}}</router-link>
                </span>
                <span class="time">{{sub_item.comment_time}}</span>
              </div>
              <p>
                <span v-html="sub_item.content"></span>
              </p>
              <div class="user-profile">
                <div class="up profile-item">
                  <Icon type="md-thumbs-up" />
                  <span class="item-text">赞一下</span>
                </div>
                <div class="reply-wrapper profile-item" @click="sub_item.isReply = ! sub_item.isReply">
                  <Icon type="ios-share-alt" />
                  <span class="item-text">回复</span>
                </div>
                <div class="down profile-item">
                  <Icon type="md-thumbs-down" />
                  <span class="item-text">踩一脚</span>
                </div>
              </div>
              <div class="sub-reply" v-if="sub_item.isReply">
                <div class="reply-input">
                  <Input :placeholder="sub_item.placeholder" v-model="replyContent" type="textarea" :rows="1" />
                  <blog-emoji @choiceEmoji="reply" :visible="sub_item.addEmoji" :height="480" :style="{borderTop: 'none', marginTop: '-1px'}"></blog-emoji>
                </div>
                <div class="reply-profile">
                  <!--<img @click="sub_item.addEmoji = !sub_item.addEmoji" class="emoji-btn" src="../../assets/emoji/emoji_res/emoji_24.png" alt="">-->
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
        article_id: this.$route.query['id'],
        replyContent: '',
        modalConfig: {
          title: '温馨提示',
          content: '你还没有输入评论哦',
          width: 400
        },
        formData: {
          nickname: ''
        }
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
          article_id: this.article_id,
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
      submitComment() {
        if (!this.commentText) return this.$Modal.warning(this.modalConfig)
        this.$store.dispatch('article/addComment', {
          id: this.article_id,
          content: this.commentText,
          comment_type: 1,
          article_id: this.article_id
        }).then(res => {
          if (res.state === 0) {
            this.commentText = ''
            this.getComment()
          }
        })
      },
      replySubmit(item, sub_item) {
        this.modalConfig.content = '你还没有输入回复哦'
        if (!this.replyContent) return this.$Modal.warning(this.modalConfig)
        this.$store.dispatch('article/addComment', {
          id: item.id,
          content: this.replyContent,
          parent: item.id,
          comment_type: 2
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
      BlogEmoji
    }
  }
</script>

<style lang="less" scoped>
  @import "./Comment";
</style>

<template>
  <div class="markdown-wrapper">
    <blog-header-top />
    <div class="edit-wrapper">
      <div class="user-wrapper">
        <div class="user">
          <div class="add-article">
            <div class="add-wrapper" @click="addArticleEvent">
              <i class="add iconfont icon-add"></i>
              <span>新建文章</span>
            </div>
            <Input placeholder="文章标题" v-model="articleTitle" v-if="addArticle"></Input>
          </div>
          <div class="category">
            <Tree :data="selfArticle" :render="renderContent">

            </Tree>
          </div>
        </div>
      </div>
      <div class="catalog-list-wrapper">
        <div class="catalog-list">
          <header class="header">{{edit ? '编辑标题': '标题'}}</header>
          <section class="list-content">
            <Input v-model="articleTitle" placeholder="标题" v-if="edit"></Input>
            <Button class="edit-ok" type="primary" v-if="edit" @click="edit = false">确认</Button>
            <div class="title" v-else>
              <span>{{articleTitle ? articleTitle : '请输入标题'}}</span>
              <span class="edit-btn" @click="edit = true">编辑</span>
            </div>
          </section>
        </div>
      </div>
      <div class="markdown-edit">
        <div class="article-desc">
          <Input type="text" v-model="articleDesc" placeholder="输入你的文章简介吧"></Input>
        </div>
        <div class="markdown-content">
          <mavon-editor code-style="atom-one-dark"
                        :subfield="subField"
                        @subfieldToggle="subFieldToggle"
                        @change="mavonChange"
                        @save="save"
                        :value="markdownContent"
          ></mavon-editor>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import {mapMutations} from 'vuex'
  import BlogHeaderTop from '../../components/HeaderTop/HeaderTop'
  import hljs from 'highlight.js/lib/highlight';
  import javascript from 'highlight.js/lib/languages/javascript';
  hljs.registerLanguage('javascript', javascript);
  export default {
    name: "Markdown",
    data() {
      return {
        subField: true,
        selfArticle: [
          {
            title: '我的文章',
            expand: true,
            render: (h, {root, node, data}) => {
              return h('span', {
                style: {
                  display: 'inline-block',
                  width: '100%'
                }
              }, [
                h('span', [
                  h('Icon', {
                    props: {
                      type: 'ios-folder-outline'
                    },
                    class: 'icon-art'
                  }),
                  h('span', {
                    class: 'first-title'
                  }, data.title),
                ]),
              ])
            },
            children: [
              {
                title: '浏览器渲染机制',
                expand: true,
              },
              {
                title: 'django',
                expand: true,
              },
              {
                title: '今天下雨了',
                expand: true,
              },
            ]
          }
        ],
        addArticle: false,
        articleTitle: '',
        articleDesc: '',
        edit: false,
        markdownContent: '',
      }
    },
    created() {
      this.getArticleDetail()
    },
    methods: {
      ...mapMutations({
        markdownSave: 'markdown/save'
      }),
      getArticleDetail() {
        const id = this.$route.query.id
        if (!id) return
        this.$store.dispatch('article/getArticleDetail', {id}).then(res => {
          this.markdownContent = res.data.markdown
          this.articleTitle = res.data.title
          this.articleDesc = res.data.desc
        })
      },
      renderContent(h, { root, node, data }) {
        return h('span', {
          style: {
            display: 'inline-block',
            width: '100%'
          }
        }, [
          h('span', [
            h('Icon', {
              props: {
                type: 'ios-paper-outline',
              },
              class: 'icon-art'
            }),
            h('em', data.title)
          ])
        ])
      },
      subFieldToggle(status, value) {
        this.subField = status
      },
      save(value, render) {
        const payload = {
          title: this.articleTitle,
          desc: this.articleDesc,
          content: render,
          markdown: value
        }
        let actionType = ''
        if (this.$route.query.id) {
          actionType = 'article/updateArticle'
          payload.id = this.$route.query.id
        } else {
          actionType = 'article/addArticle'
        }
        this.$store.dispatch(actionType, payload).then(res => {
          this.$Message.success(res.message)
        })
      },
      addArticleEvent() {
        this.addArticle = !this.addArticle
      },
      mavonChange(val) {
      }
    },
    components: {
      BlogHeaderTop,
    }
  }
</script>

<style lang="less" scoped>
 @import "./Markdown";
</style>

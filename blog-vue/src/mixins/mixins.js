export default {
  methods: {
    getArticleDetail() {
      const id = this.$route.params.id
      this.$store.dispatch('article/article', {
        body: {
          id
        }
      }).then(res => {
        this.article = res.data
        this.postLookCount(res.data.look_count + 1)
        this.setHighlight()
      })
    },
    postLookCount(look_count) {
      this.$store.dispatch('article/article', {
        method: 'PATCH',
        body: {
          look_count,
          id: this.$route.params.id
        }
      })
    },
    setHighlight() {
      this.$nextTick(() => {
        const pres = document.querySelectorAll('pre')
        const body = document.querySelector('.markdown-body')
        if (body.children.length > 0) {
          const arr = Array.from(body.children).filter(item => item.tagName === 'P' || item.tagName.includes('H'))
          if (arr.length === Array.from(body.children).length) {
            Array.from(body.children).forEach(item => {
              if (item.tagName === 'P') {
                item.classList.add('text-indent')
              }
            })
          }
        }
        Array.from(pres).map(item => {
          const code = item.querySelector('code')
          if (!item.className && !code.className) {
            item.className = 'padding'
          }
        })
      })
    },
  }
}

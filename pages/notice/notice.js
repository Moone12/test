Page({
  data: {
    noticeList: [], // 公告列表
    isLoading: false // 加载状态
  },

  onLoad() {
    this.getNoticeList();
  },

  // 获取公告列表
  getNoticeList() {
    this.setData({ isLoading: true });
    // 假设后端接口地址为 https://yourserver.com/api/notice/list
    wx.request({
      url: 'https://yourserver.com/api/notice/list',
      success: (res) => {
        if (res.statusCode === 200) {
          this.setData({
            noticeList: res.data.data,
            isLoading: false
          });
        } else {
          wx.showToast({
            title: '获取公告失败',
            icon: 'none'
          });
          this.setData({ isLoading: false });
        }
      },
      fail: () => {
        wx.showToast({
          title: '网络请求失败',
          icon: 'none'
        });
        this.setData({ isLoading: false });
      }
    });
  },

  // 跳转到公告详情页
  goToNoticeDetail(e) {
    const noticeId = e.currentTarget.dataset.id;
    wx.navigateTo({
      url: `/pages/noticeDetail/noticeDetail?id=${noticeId}`
    });
  },

  onPullDownRefresh() {
    this.getNoticeList();
    wx.stopPullDownRefresh();
  },

  onReachBottom() {
    // 这里可以添加加载更多公告的逻辑
  }
});
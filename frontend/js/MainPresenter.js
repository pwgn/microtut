function MainPresenter(view) {

    this.view = view;
    this.view.setPresenter(this);

}

MainPresenter.prototype.start = function() {
    console.log('start');
};

function go_to_all() {
    self.location = '/users';
}

function go_add() {
    self.location = '/create';
}

function go_edit(id) {
    self.location = '/user/edit/' + id;
}

function go_delete(id) {
    self.location = '/user/' + id + '/delete';
}

function get_one(id) {
    self.location = '/user/' + id;
}
function solution(new_id) {
    let reg = /[`~!@#$%^&*()|+\=?;,:'"<>\{\}\[\]\\\/ ]/gim;
    
    new_id = new_id.toLowerCase();
    new_id = new_id.replace(reg, "");
    new_id = new_id.split('.').filter((item) => item != "").join(".");
    new_id = new_id.length <= 0 ? 'a' : new_id;
    new_id = new_id.slice(0, 15);
    new_id = new_id.split('.').filter((item) => item != "").join(".");
    new_id = new_id.length <= 2 ? new_id.padEnd(3, new_id.slice(-1)) : new_id;
    
    return new_id;
}
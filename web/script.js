"use strict";

const sb_tb = 500;
const tb_fb = 1000;

const clientWidth = window.clientWidth;

const IsSb = clientWidth <= sb_tb;
const IsTb = !IsSb && clientWidth <= tb_fb;
const IsFb = !(IsSb || IsTb);

const IsSbTb = IsSb || IsTb;
const IsTbFb = IsTb || IsFb;


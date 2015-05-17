title: Фильтры на сайте, смена классов при клике.
date: 2012-09-24
type: blog
tags: [javascript, jquery, Снипеты]

Есть необходимость фильтровать что либо, например товары по цене. И фильтры бывают разные. Два, три или более кликов. Если говорить о простых фильтрах и смене класса у ссылки, проблем нет вообще, `.toggleClass( className )`, а если больше кликов?

Я нашел в интернете много решений, но одно из них мне показалось наиболее изящным. Довольно простой скрипт для смены классов. 

<style type="text/css">
.ex_sortlink .none:after {
    content: "";
}
.ex_sortlink .up:after {
    content: "↑";
    margin-left: .2em;
}
.ex_sortlink .down:after {
    content: "↓";
    margin-left: .2em;
}
.ex_sortlink2 .state1 {color: red;}
.ex_sortlink2 .state2 {color: green;}
.ex_sortlink2 .state3 {color: black;}
.ex_sortlink2 .state4 {color: blue;}
</style>
<script type="text/javascript">
$(function(){
    $('.none, .up, .down').click(function() {                             
        this.className = {
           down : 'none', none: 'up', up: 'down'
        }[this.className];
        return false;
    });

    $('.ex_sortlink2 a').click(function(){
      var state = this.className;
      state = state.split('state');
      state = state[1];
      state = parseInt(state);
      state = (state + 1) % 5;
      this.className = "state" + state;
      return false;
    });
})
</script>

Довольно удобно сортировать по цене, от низкой к высокой, или по алфавиту. И так далее.
<div class="ex_sortlink">
    <a href="" class="none">Цена</a>
</div>

    <script type="text/javascript">
    $(function(){
        $('.none, .up, .down').click(function() {                             
            this.className = {
               down : 'none', none: 'up', up: 'down'
            }[this.className];
            return false;
        });
    })
    </script>
    <div class="ex_sortlink">
        <a href="" class="none">Цена</a>
    </div>


Но если вам нужно скажем 4 или 6, 7 классов? Тогда 1-й скрипт не подойдет, точнее подойдет, но можно будет запутаться в коде. Но мне коллега подсказал другое решение.

<div class="ex_sortlink2">
    <a href="" class="state0">Цвета</a>
</div>

    <script type="text/javascript">
    $(function(){
        $('.ex_sortlink2 a').click(function(){
          var state = this.className;
          state = state.split('state');
          state = state[1];
          state = parseInt(state);
          state = (state + 1) %  5;
          this.className = "state" + state;
          return false;
        });
    })
    </script>

    <div class="ex_sortlink2">
        <a href="" class="state0">Цвета</a>
    </div>

Отдельное спасибо [Вадику Растягаеву](http://www.facebook.com/oktoberliner).
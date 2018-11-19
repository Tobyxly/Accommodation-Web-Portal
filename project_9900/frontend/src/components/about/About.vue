<template>
  <div class="container">
    <div class="row mb-5">
      <div class="col-4">
        <!--导航-->
        <br><br><br>
        <div class="list-group mb-5">
          <router-link tag="li" class="nav-link" to="/history">
            <a class="list-group-item list-group-item-action">History order</a>
          </router-link>
          <br>
          <router-link tag="li" class="nav-link" to="/contact">
            <a class="list-group-item list-group-item-action">Contact us</a>
          </router-link>
        </div>
      </div>

      <div class="col-8">
        <!--导航所对应的内容-->
        <router-view></router-view>
      </div>
    </div>

    <div class="row">
        <div class="col-4">
          <img src="src/assets/p.png">
          <br><br>
          <h4>Search From Anywhere</h4>
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla convallis egestas rhoncus. Donec facilisis fermentum sem, ac viverra ante luctus vel.</p>
        </div>
        <div class="col-4">
          <img src="src/assets/p1.png">
          <br><br>
          <h4>Friendly Agents</h4>
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla convallis egestas rhoncus. Donec facilisis fermentum sem, ac viverra ante luctus vel.</p>
        </div>
        <div class="col-4">
          <img src="src/assets/p2.png">
          <br><br>
          <h4>Buy or Rent</h4>
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla convallis egestas rhoncus. Donec facilisis fermentum sem, ac viverra ante luctus vel.</p>
        </div>
    </div>




  </div>
</template>
<script>
    export default {
        name: "About"
    }
</script>

<style scoped>

</style>

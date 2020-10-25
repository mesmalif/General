{% extends "layout.html" %}
{% block content %}
    <div class="content-section">
      <form class="" action="" method="post">
        {{ form.hidden_tag() }}
        <fieldset class="form-group">
          <legend class="border-bottom mb-4"> Join Today</legend>
          <div class="form-group">
            {{ form.username.label(class="form-control-label") }}
            {{ form.username(class="form-control-label form-control-lg") }}
          </div>
          <div class="form-group">
            {{ form.email.label(class="form-control-label") }}
            {{ form.email(class="form-control-label form-control-lg") }}
          </div>
          <div class="form-group">
            {{ form.password.label(class="form-control-label") }}
            {{ form.password(class="form-control-label form-control-lg") }}
          </div>
          <div class="form-group">
            {{ form.confirm_password.label(class="form-control-label") }}
            {{ form.confirm_password(class="form-control-label form-control-lg") }}
          </div>
        </fieldset>
        <div class="form-group">
          {{form.submit(class="btn btn-outline-info")}}
        </div>
      </form>
    </div>
    <div class="border-top pt-3">
      <small class="text-muted">Already have account?</small><a class="ml-2" href="{{url_for('login')}}"> Sign In</a>
    </div>
{% endblock content %}

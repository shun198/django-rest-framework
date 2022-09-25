/       rest_framework.routers.view     api-root
/\.<format>/    rest_framework.routers.view     api-root
/admin/ django.contrib.admin.sites.index        admin:index
/admin/<app_label>/     django.contrib.admin.sites.app_index    admin:app_list
/admin/<url>    django.contrib.admin.sites.catch_all_view
/admin/auth/group/      django.contrib.admin.options.changelist_view    admin:auth_group_changelist
/admin/auth/group/<path:object_id>/     django.views.generic.base.view
/admin/auth/group/<path:object_id>/change/      django.contrib.admin.options.change_view        admin:auth_group_change
/admin/auth/group/<path:object_id>/delete/      django.contrib.admin.options.delete_view        admin:auth_group_delete
/admin/auth/group/<path:object_id>/history/     django.contrib.admin.options.history_view       admin:auth_group_history
/admin/auth/group/add/  django.contrib.admin.options.add_view   admin:auth_group_add
/admin/auth/user/       django.contrib.admin.options.changelist_view    admin:auth_user_changelist
/admin/auth/user/<id>/password/ django.contrib.auth.admin.user_change_password  admin:auth_user_password_change
/admin/auth/user/<path:object_id>/      django.views.generic.base.view
/admin/auth/user/<path:object_id>/change/       django.contrib.admin.options.change_view        admin:auth_user_change
/admin/auth/user/<path:object_id>/delete/       django.contrib.admin.options.delete_view        admin:auth_user_delete
/admin/auth/user/<path:object_id>/history/      django.contrib.admin.options.history_view       admin:auth_user_history
/admin/auth/user/add/   django.contrib.auth.admin.add_view      admin:auth_user_add
/admin/autocomplete/    django.contrib.admin.sites.autocomplete_view    admin:autocomplete
/admin/jsi18n/  django.contrib.admin.sites.i18n_javascript      admin:jsi18n
/admin/login/   django.contrib.admin.sites.login        admin:login
/admin/logout/  django.contrib.admin.sites.logout       admin:logout
/admin/password_change/ django.contrib.admin.sites.password_change      admin:password_change
/admin/password_change/done/    django.contrib.admin.sites.password_change_done admin:password_change_done
/admin/r/<int:content_type_id>/<path:object_id>/        django.contrib.contenttypes.views.shortcut      admin:view_on_site
/admin/relationships/user/      django.contrib.admin.options.changelist_view    admin:relationships_user_changelist
/admin/relationships/user/<path:object_id>/     django.views.generic.base.view
/admin/relationships/user/<path:object_id>/change/      django.contrib.admin.options.change_view        admin:relationships_user_change
/admin/relationships/user/<path:object_id>/delete/      django.contrib.admin.options.delete_view        admin:relationships_user_delete
/admin/relationships/user/<path:object_id>/history/     django.contrib.admin.options.history_view       admin:relationships_user_history
/admin/relationships/user/add/  django.contrib.admin.options.add_view   admin:relationships_user_add
/api/schema/    drf_spectacular.views.view      schema
/docs/  drf_spectacular.views.view      swagger-ui
/redoc/ drf_spectacular.views.view      redoc
/users/ relationships.views.UserViewSets        user-list
/users/<pk>/    relationships.views.UserViewSets        user-detail
/users/<pk>\.<format>/  relationships.views.UserViewSets        user-detail
/users\.<format>/       relationships.views.UserViewSets        user-list


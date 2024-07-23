path('<int:pk>/edit/', views.comic_edit, name='comic_edit'),
    path('<int:pk>/detail/', views.comic_detail, name='comic_detail'),
    path('<int:pk>/add_panel/', views.panel_add, name='panel_add'),
    path('<int:pk>/edit_panel/<int:panel_pk>/', views.panel_edit, name='panel_edit'),
    path('<int:pk>/delete_panel/<int:panel_pk>/', views.panel_delete, name='panel_delete'),
]
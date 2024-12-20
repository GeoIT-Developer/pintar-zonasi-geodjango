from django.urls import path
from .views import (
    ProjectMetadataList,
    ProjectMetadataDetail,
    ProjectCreate,
    ProjectMetadataDelete,
    ProjectSaveLayer,
    ProjectUpdateStatus,
    ProjectListZonasi,
    ProjectFindZonasi,
)

urlpatterns = [
    path(
        "project/create/",
        ProjectCreate.as_view(),
        name="project-create",
    ),
    path(
        "project/delete/<str:pk>/",
        ProjectMetadataDelete.as_view(),
        name="project-delete",
    ),
    path("project/", ProjectMetadataList.as_view(), name="project-list"),
    path(
        "project/zonasi/",
        ProjectListZonasi.as_view(),
        name="project-list-zonasi",
    ),
    path(
        "project/zonasi/<str:pk>/",
        ProjectFindZonasi.as_view(),
        name="project-find-zonasi",
    ),
    path(
        "project/<str:pk>/",
        ProjectMetadataDetail.as_view(),
        name="project-metadata-detail",
    ),
    path(
        "project/save-layer/<str:pk>/",
        ProjectSaveLayer.as_view(),
        name="project-save-layer",
    ),
    path(
        "project/update-status/<str:pk>/<str:status>/",
        ProjectUpdateStatus.as_view(),
        name="project-change-status",
    ),
]

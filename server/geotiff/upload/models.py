from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.db import models
import gdal2tiles


class GeoTiff(models.Model):
    source_file = models.FileField(
        upload_to='uploads/',
        validators=[FileExtensionValidator(allowed_extensions=['tif', 'png'])]
    )

    def get_tiles_path(self):
        return 'uploads/tiles/' + str(self.id)

    def save(self, *args, **kwargs):
        super(GeoTiff, self).save(*args, **kwargs)
        try:
            gdal2tiles.generate_tiles(self.source_file.path,
                                      self.get_tiles_path())
        except:
            raise ValidationError(message='Could not convert to tiles')

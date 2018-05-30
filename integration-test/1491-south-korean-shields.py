from . import FixtureTest


class SouthKoreanShields(FixtureTest):
    def test_asianhighway(self):
        import dsl

        z, x, y = (16, 55875, 25370)

        self.generate_fixtures(
            dsl.is_in('KR', z, x, y),
            # https://www.openstreetmap.org/way/547188348
            dsl.way(547188348, dsl.tile_diagonal(z, x, y), {
                'name:en': 'Tongil-ro', 'name': u'\ud1b5\uc77c\ub85c',
                'review': 'no', 'source': 'openstreetmap.org',
                'highway': 'primary',
            }),
            dsl.relation(1, {
                'alt_name': u'\uc544\uc8fc\uacf5\ub85c 1\ud638\uc120',
                'int_ref': 'AH1', 'layer': '1', 'section': 'Korea',
                'int_name': 'Asian Highway AH1', 'network': 'AH',
                'name': u'\uc544\uc2dc\uc548 \ud558\uc774\uc6e8\uc774 1'
                u'\ud638\uc120', 'name:en': 'Asian Highway AH1', 'ref': 'AH1',
                'route': 'road', 'source': 'openstreetmap.org',
                'state': 'connection', 'type': 'route',
                'wikidata': 'Q494205', 'wikipedia': 'en:AH1',
            }, ways=[547188348]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 547188348,
                'shield_text': '1',
                'network': 'AsianHighway',
            })

    def test_asianhighway_no_relation(self):
        import dsl

        z, x, y = (16, 55886, 25381)

        self.generate_fixtures(
            dsl.is_in('KR', z, x, y),
            # https://www.openstreetmap.org/way/37399710
            dsl.way(37399710, dsl.tile_diagonal(z, x, y), {
                'tunnel:name:ko_rm': 'Namsan il ho teoneol', 'tunnel': 'yes',
                'layer': '-2', 'name:en': 'Samil-daero',
                'name': u'\uc0bc\uc77c\ub300\ub85c',
                'tunnel:name:ko': u'\ub0a8\uc0b01\ud638\ud130\ub110',
                'name:ko': u'\uc0bc\uc77c\ub300\ub85c', 'review': 'no',
                'name:ko_rm': 'Samil-daero',
                'tunnel:name:en': 'Namsan 1 Ho Tunnel',
                'source': 'openstreetmap.org',
                'ncat': u'\uad11\uc5ed\uc2dc\ub3c4\ub85c', 'oneway': 'yes',
                'tunnel:name': u'\ub0a8\uc0b01\ud638\ud130\ub110',
                'ref': 'AH1', 'toll': 'yes', 'highway': 'primary',
                'name:ja': u'\u4e09\u4e00\u5927\u8def',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 37399710,
                'shield_text': '1',
                'network': 'AsianHighway',
            })

    def test_kr_expressway_rel_no_net(self):
        import dsl

        z, x, y = (16, 55975, 25658)

        self.generate_fixtures(
            dsl.is_in('KR', z, x, y),
            # https://www.openstreetmap.org/way/90611594
            dsl.way(90611594, dsl.tile_diagonal(z, x, y), {
                'name:en': u'Tongyeong\u2013Daejeon Expressway', 'lanes': '2',
                'name': u'\ud1b5\uc601\ub300\uc804\uace0\uc18d\ub3c4\ub85c',
                'name:ko': u'\ud1b5\uc601\ub300\uc804\uace0\uc18d\ub3c4\ub85c',
                'name:ko_rm': 'Tongyeong-daejeon-gosokdoro',
                'source': 'openstreetmap.org', 'maxspeed': '100',
                'oneway': 'yes', 'ref': '35', 'highway': 'motorway',
            }),
            dsl.relation(1, {
                'layer': '1', 'name:en': u'Tongyeong\u2013Daejeon Expressway',
                'name': u'\ud1b5\uc601\ub300\uc804\uace0\uc18d\ub3c4\ub85c',
                'name:ko': u'\ud1b5\uc601\ub300\uc804\uace0\uc18d\ub3c4\ub85c',
                'type': 'route', 'route': 'road',
                'source': 'openstreetmap.org', 'ref': '35',
            }, ways=[90611594]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 90611594,
                'shield_text': '35',
                'network': 'KR:expressway',
            })

    def test_kr_expressway(self):
        import dsl

        z, x, y = (16, 55904, 25415)

        self.generate_fixtures(
            dsl.is_in('KR', z, x, y),
            # https://www.openstreetmap.org/way/59242897
            dsl.way(59242897, dsl.tile_diagonal(z, x, y), {
                'name:en': 'Seoul Ring Expressway', 'lanes': '4',
                'name': u'\uc11c\uc6b8\uc678\uacfd\uc21c\ud658\uace0'
                u'\uc18d\ub3c4\ub85c', 'name:ko': u'\uc11c\uc6b8\uc678'
                u'\uacfd\uc21c\ud658\uace0\uc18d\ub3c4\ub85c',
                'name:ko_rm': 'Seouloegwaksunhwangosokdoro',
                'source': 'openstreetmap.org', 'oneway': 'yes', 'ref': '100',
                'highway': 'motorway',
            }),
            dsl.relation(1, {
                'name:en': 'Seoul Ring Expressway(KEC), bound for '
                'Pangyo(Ilsan)', 'name': u'\uc11c\uc6b8\uc678\uacfd\uc21c'
                u'\ud658\uace0\uc18d\ub3c4\ub85c(\ub3c4\ub85c\uacf5\uc0ac)'
                u' \ud310\uad50(\uc77c\uc0b0)\ubc29\ud5a5',
                'name:ko': u'\uc11c\uc6b8\uc678\uacfd\uc21c\ud658\uace0'
                u'\uc18d\ub3c4\ub85c(\ub3c4\ub85c\uacf5\uc0ac) \ud310'
                u'\uad50(\uc77c\uc0b0)\ubc29\ud5a5', 'route': 'road',
                'source': 'openstreetmap.org',
                'operator': 'Korea Expressway Corporation', 'type': 'route',
                'road': 'kr:expressway', 'network': 'KR:expressway',
            }, ways=[59242897]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 59242897,
                'shield_text': '100',
                'network': 'KR:expressway',
            })

    def test_kr_national(self):
        import dsl

        z, x, y = (16, 55864, 25396)

        self.generate_fixtures(
            dsl.is_in('KR', z, x, y),
            # https://www.openstreetmap.org/way/71503022
            dsl.way(71503022, dsl.tile_diagonal(z, x, y), {
                'name:en': 'Nambusunhwan-ro', 'name': u'\ub0a8\ubd80'
                u'\uc21c\ud658\ub85c', 'name:ko': u'\ub0a8\ubd80\uc21c'
                u'\ud658\ub85c', 'source': 'openstreetmap.org',
                'oneway': 'yes', 'ref': '92', 'highway': 'primary',
                'name:ja': u'\u5357\u90e8\u5faa\u74b0\u8def',
            }),
            dsl.relation(1, {
                'type': 'route', 'route': 'road', 'ref': '92',
                'network': 'KR:national', 'source': 'openstreetmap.org',
            }, ways=[71503022]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 71503022,
                'shield_text': '92',
                'network': 'KR:national',
            })

    def test_kr_national_no_rel(self):
        import dsl

        z, x, y = (16, 56158, 25837)

        self.generate_fixtures(
            dsl.is_in('KR', z, x, y),
            # https://www.openstreetmap.org/way/542451694
            dsl.way(542451694, dsl.tile_diagonal(z, x, y), {
                'name:en': 'Upo 1-daero', 'name': u'\uc6b0\ud3ec1\ub300\ub85c',
                'name:ko': u'\uc6b0\ud3ec1\ub300\ub85c', 'review': 'no',
                'source': 'openstreetmap.org', 'highway': 'primary',
                'ref': '20;24', 'ncat': u'\uad6d\ub3c4',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 542451694,
                'shield_text': '20', 'network': 'KR:national',
                'all_shield_texts': ['20', '24'],
                'all_networks': ['KR:national', 'KR:national'],
            })

    def test_kr_expressway_no_rel(self):
        import dsl

        z, x, y = (16, 55923, 25876)

        self.generate_fixtures(
            dsl.is_in('KR', z, x, y),
            # https://www.openstreetmap.org/way/574671133
            dsl.way(574671133, dsl.tile_diagonal(z, x, y), {
                'name:en': 'Gwangjudaegu Expressway',
                'name': u'\uad11\uc8fc\ub300\uad6c\uace0\uc18d\ub3c4\ub85c',
                'name:ko': u'\uad11\uc8fc\ub300\uad6c\uace0\uc18d\ub3c4\ub85c',
                'review': 'no', 'name:ko_rm': 'Gwangjudaegugosokdoro',
                'source': 'openstreetmap.org', 'maxspeed': '80',
                'ncat': u'\uace0\uc18d\ub3c4\ub85c', 'oneway': 'yes',
                'ref': '12', 'highway': 'motorway',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 574671133,
                'shield_text': '12',
                'network': 'KR:expressway',
            })

    def test_kr_expressway_no_name_en(self):
        import dsl

        z, x, y = (16, 56165, 25760)

        self.generate_fixtures(
            dsl.is_in('KR', z, x, y),
            # https://www.openstreetmap.org/way/43543281
            dsl.way(43543281, dsl.tile_diagonal(z, x, y), {
                'lanes': '2', 'name': u'\uc911\ubd80\ub0b4\ub959\uace0'
                u'\uc18d\ub3c4\ub85c\uc9c0\uc120', 'review': 'no',
                'source': 'openstreetmap.org', 'highway': 'motorway',
                'oneway': 'yes', 'ref': '451',
                'ncat': u'\uace0\uc18d\ub3c4\ub85c',
            }),
            dsl.relation(1, {
                'type': 'route', 'route': 'road', 'ref': '451',
                'source': 'openstreetmap.org',
            }, ways=[43543281]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 43543281,
                'shield_text': '451',
                'network': 'KR:expressway',
            })

    def test_kr_expressway_no_name_en_no_ncat(self):
        # same as the test above, but without the "ncat" to test that it
        # backfills from the name.
        import dsl

        z, x, y = (16, 56165, 25760)

        self.generate_fixtures(
            dsl.is_in('KR', z, x, y),
            # https://www.openstreetmap.org/way/43543281
            dsl.way(43543281, dsl.tile_diagonal(z, x, y), {
                'lanes': '2', 'name': u'\uc911\ubd80\ub0b4\ub959\uace0'
                u'\uc18d\ub3c4\ub85c\uc9c0\uc120', 'review': 'no',
                'source': 'openstreetmap.org', 'highway': 'motorway',
                'oneway': 'yes', 'ref': '451',
            }),
            dsl.relation(1, {
                'type': 'route', 'route': 'road', 'ref': '451',
                'source': 'openstreetmap.org',
            }, ways=[43543281]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 43543281,
                'shield_text': '451',
                'network': 'KR:expressway',
            })

    def test_kr_jungbunaeryukgosokdoro(self):
        import dsl

        z, x, y = (16, 56156, 25839)

        self.generate_fixtures(
            dsl.is_in('KR', z, x, y),
            # https://www.openstreetmap.org/way/562319872
            dsl.way(562319872, dsl.tile_diagonal(z, x, y), {
                'name:en': 'Jungbunaeryuk Expressway', 'lanes': '2',
                'name': u'\uc911\ubd80\ub0b4\ub959\uace0\uc18d\ub3c4\ub85c',
                'name:ko': u'\uc911\ubd80\ub0b4\ub959\uace0\uc18d\ub3c4\ub85c',
                'review': 'no', 'name:ko_rm': 'Jungbunaeryukgosokdoro',
                'source': 'openstreetmap.org',
                'ncat': u'\uace0\uc18d\ub3c4\ub85c', 'oneway': 'yes',
                'ref': '45', 'toll': 'yes', 'highway': 'motorway',
            }),
            dsl.relation(1, {
                'name:en': 'Jungbunaeryuk Expressway',
                'name': u'\uc911\ubd80\ub0b4\ub959\uace0\uc18d\ub3c4\ub85c',
                'name:ko': u'\uc911\ubd80\ub0b4\ub959\uace0\uc18d\ub3c4\ub85c',
                'ref': '45', 'route': 'road', 'source': 'openstreetmap.org',
                'type': 'route',
            }, ways=[562319872]),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 562319872,
                'shield_text': '45',
                'network': 'KR:expressway',
            })

    def test_kr_upo_2_ro(self):
        import dsl

        z, x, y = (16, 56158, 25837)

        self.generate_fixtures(
            dsl.is_in('KR', z, x, y),
            # https://www.openstreetmap.org/way/179815107
            dsl.way(179815107, dsl.tile_diagonal(z, x, y), {
                'name:en': 'Upo 2-ro', 'name': u'\uc6b0\ud3ec2\ub85c',
                'name:ko': u'\uc6b0\ud3ec2\ub85c', 'review': 'no',
                'source': 'openstreetmap.org', 'highway': 'secondary',
                'ref': '1080', 'ncat': u'\uc9c0\ubc29\ub3c4',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 179815107,
                'shield_text': '1080',
                'network': 'KR:local',
            })

    def test_kr_special_city(self):
        import dsl

        z, x, y = (16, 55879, 25372)

        self.generate_fixtures(
            dsl.is_in('KR', z, x, y),
            # https://www.openstreetmap.org/way/37395768
            dsl.way(37395768, dsl.tile_diagonal(z, x, y), {
                'bridge': 'viaduct', 'layer': '2',
                'name:en': 'Naebusunhwan-ro', 'bicycle': 'no',
                'name': u'\ub0b4\ubd80\uc21c\ud658\ub85c',
                'name:ko': u'\ub0b4\ubd80\uc21c\ud658\ub85c', 'review': 'no',
                'source': 'openstreetmap.org',
                'ncat': u'\ud2b9\ubcc4\uc2dc\ub3c4', 'oneway': 'yes',
                'ref': '30', 'highway': 'trunk',
                'name:ja': u'\u5185\u90e8\u5faa\u74b0\u8def',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 37395768,
                'shield_text': '30',
                'network': 'KR:metropolitan',
            })

    def test_kr_metropolitan(self):
        import dsl

        z, x, y = (16, 56178, 25761)

        self.generate_fixtures(
            dsl.is_in('KR', z, x, y),
            # https://www.openstreetmap.org/way/577716125
            dsl.way(577716125, dsl.tile_diagonal(z, x, y), {
                'name:en': 'Jungang-daero',
                'name': u'\uc911\uc559\ub300\ub85c',
                'name:ko': u'\uc911\uc559\ub300\ub85c', 'review': 'no',
                'name:ko_rm': 'Jungangdaero', 'source': 'openstreetmap.org',
                'highway': 'primary', 'ref': '61',
                'ncat': u'\uad11\uc5ed\uc2dc\ub3c4\ub85c',
            }),
        )

        self.assert_has_feature(
            z, x, y, 'roads', {
                'id': 577716125,
                'shield_text': '61',
                'network': 'KR:metropolitan',
            })
